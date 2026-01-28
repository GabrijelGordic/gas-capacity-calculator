import streamlit as st
import json
import os

# 1. PAGE SETUP
st.set_page_config(page_title="Gas Specific Heat Capacity", layout="centered")

# 2. CUSTOM STYLING - Crystal Hydrogen Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&family=Exo+2:wght@400;500;600;700&display=swap');
    
    /* Background */
    .stApp {
        background: 
            radial-gradient(circle at 15% 15%, rgba(126, 200, 227, 0.2) 0%, transparent 35%),
            radial-gradient(circle at 85% 20%, rgba(77, 168, 218, 0.15) 0%, transparent 30%),
            radial-gradient(circle at 25% 75%, rgba(184, 223, 240, 0.2) 0%, transparent 40%),
            linear-gradient(180deg, #e8f4fc 0%, #d4eaf7 30%, #c5e3f5 60%, #b8dff0 100%);
        background-attachment: fixed;
    }
    
    /* Main container */
    .main .block-container {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.88), rgba(232, 244, 252, 0.92));
        border: 1px solid rgba(77, 168, 218, 0.25);
        border-radius: 24px;
        padding: 2.5rem 3rem;
        box-shadow: 0 8px 32px rgba(43, 124, 186, 0.12);
        margin-top: 2rem;
    }
    
    /* Title */
    h1 {
        font-family: 'Exo 2', sans-serif !important;
        background: linear-gradient(135deg, #1a5a8a, #2b7cba, #4da8da);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 2rem !important;
        font-weight: 600 !important;
    }
    
    h2, h3 {
        font-family: 'Exo 2', sans-serif !important;
        color: #2b7cba !important;
    }
    
    p, span, label {
        font-family: 'Quicksand', sans-serif !important;
        color: #3a6d8c !important;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(77, 168, 218, 0.5), transparent);
    }
    
    /* Selectbox - make it match result container height */
    .stSelectbox > div > div {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(232, 244, 252, 0.9)) !important;
        border: 1.5px solid rgba(77, 168, 218, 0.35) !important;
        border-radius: 12px !important;
        color: #2b7cba !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 600 !important;
        min-height: 42px !important;
    }
    
    /* Center text in selectbox */
    .stSelectbox [data-baseweb="select"] > div {
        justify-content: center !important;
    }
    
    .stSelectbox [data-baseweb="select"] [data-testid="stMarkdownContainer"],
    .stSelectbox [data-baseweb="select"] span {
        text-align: center !important;
        width: 100% !important;
        padding-right: 24px !important;
    }
    
    /* Result container - make it fill width and match selectbox */
    [data-testid="stCode"] {
        width: 100% !important;
    }
    
    [data-testid="stCode"] > div {
        width: 100% !important;
    }
    
    [data-testid="stCode"] pre {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(232, 244, 252, 0.9)) !important;
        border: 1.5px solid rgba(77, 168, 218, 0.35) !important;
        border-radius: 12px !important;
        min-height: 42px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0.5rem 1rem !important;
    }
    
    [data-testid="stCode"] code {
        background: transparent !important;
        color: #1a5a8a !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        text-align: center !important;
        width: 100% !important;
        white-space: nowrap !important;
    }
    
    /* Number input */
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 1.5px solid rgba(77, 168, 218, 0.35) !important;
        border-radius: 12px !important;
        color: #1a5a8a !important;
        font-family: 'Exo 2', sans-serif !important;
        font-weight: 600 !important;
    }
    
    .stNumberInput button {
        background: linear-gradient(145deg, #7ec8e3, #5ab5d8) !important;
        border: none !important;
        color: white !important;
    }
    
    /* Dropdown menu */
    [data-baseweb="menu"] {
        background: rgba(255, 255, 255, 0.98) !important;
        border-radius: 12px !important;
    }
    
    [data-baseweb="menu"] li {
        color: #3a6d8c !important;
        font-family: 'Quicksand', sans-serif !important;
        justify-content: center !important;
        text-align: center !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background: rgba(126, 200, 227, 0.25) !important;
    }
    
    /* Hide branding */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. LOAD DATA FROM JSON
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

# 5. INTERPOLATION LOGIC
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

# 6. USER INTERFACE (UI)
st.title("Mean Molar Specific Heat Capacity of Ideal Gases")
st.write("Between temperatures 0°C and t°C")

st.divider()

# Temperature Input
col_temp1, col_temp2 = st.columns([1, 2])
with col_temp1:
    st.subheader("Temperature (°C):")
with col_temp2:
    target_temp = st.number_input("Enter temperature", value=0.0, step=1.0, format="%.2f", label_visibility="collapsed")

st.divider()

if gas_data:
    # Gas list for dropdown
    gas_options = ["Select gas"] + list(gas_data.keys())

    st.subheader("Calculation (kJ/kmolK):")

    # Loop for 6 input rows
    for i in range(6):
        c1, c2 = st.columns(2)  # Equal width columns
        
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
            # Always show the result container
            if result is not None and result != "":
                st.code(f"{result}", language=None)
            else:
                st.code("—", language=None)  # Show placeholder dash 
else:
    st.warning("Gas data not loaded.")

st.divider()
st.caption("💧 Data source: gasses.json | Thermodynamic Properties Database")