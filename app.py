import streamlit as st
import json
import os

# 1. PAGE SETUP
st.set_page_config(page_title="Gas Specific Heat Capacity", layout="centered")

# 2. LOAD DATA FROM JSON
@st.cache_data # Cache data to prevent reloading on every interaction
def load_gas_data():
    filename = 'gasses.json'
    
    # Check if file exists
    if not os.path.exists(filename):
        st.error(f"File {filename} not found! Please check if it exists in the same folder as app.py.")
        return {}

    try:
        with open(filename, 'r') as f:
            raw_data = json.load(f)
            
        # CONVERSION: JSON keys are always strings ("100"), 
        # but we need integers (100) for the math logic.
        processed_data = {}
        for gas_name, temp_dict in raw_data.items():
            # Create a new dictionary where keys are integers
            processed_data[gas_name] = {int(t): v for t, v in temp_dict.items()}
            
        return processed_data
        
    except Exception as e:
        st.error(f"Error loading JSON: {e}")
        return {}

# Load data into variable
gas_data = load_gas_data()

# 3. INTERPOLATION LOGIC
def get_interpolated_value(gas_name, temp):
    """Calculates specific heat capacity using linear interpolation."""
    if not gas_name or gas_name == "Select gas":
        return None
        
    data = gas_data.get(gas_name)
    if not data:
        return "No data"
    
    # Check if exact value exists
    if temp in data:
        val = data[temp]
        # Check for empty string (e.g., h2o at 3000)
        if val == "": 
            return "N/A"
        return val
    
    # Linear Interpolation logic
    sorted_keys = sorted(data.keys())
    
    # Check bounds (Range check)
    if temp < sorted_keys[0] or temp > sorted_keys[-1]:
        return "Out of range"

    next_lower = None
    next_higher = None
    
    for key in sorted_keys:
        if key <= temp:
            next_lower = key
        else:
            next_higher = key
            break
            
    if next_lower is not None and next_higher is not None:
        y1 = float(data[next_lower])
        y2 = float(data[next_higher])
        x1 = float(next_lower)
        x2 = float(next_higher)
        
        # Formula: y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
        res = y1 + (y2 - y1) / (x2 - x1) * (temp - x1)
        return round(res, 3)
    
    return "Error"

# 4. USER INTERFACE (UI)
st.title("Mean Molar Specific Heat Capacity of Ideal Gases")
st.write("Between temperatures 0°C and t°C")

st.divider()

# Temperature Input
col_temp1, col_temp2 = st.columns([1, 2])
with col_temp1:
    st.subheader("Temperature (°C):")
with col_temp2:
    target_temp = st.number_input("Enter temperature", value=0, step=10, label_visibility="collapsed")

st.divider()

if gas_data:
    # Gas list for dropdown
    gas_options = ["Select gas"] + list(gas_data.keys())

    st.subheader("Calculation (kJ/kmolK):")

    # Loop for 6 input rows
    for i in range(6):
        c1, c2 = st.columns([3, 2])
        
        with c1:
            # Dropdown for gas selection
            selected_gas = st.selectbox(
                f"Gas {i+1}", 
                options=gas_options, 
                key=f"gas_select_{i}",
                label_visibility="collapsed"
            )
        
        with c2:
            result = get_interpolated_value(selected_gas, target_temp)
            
            if result is not None and result != "":
                # Display result in code block (enables copy button)
                st.code(f"{result}", language=None) 
            else:
                # Spacer to keep layout structure
                st.text("") 
else:
    st.warning("Gas data not loaded.")

st.divider()
st.caption("Data loaded from 'gasses.json'")