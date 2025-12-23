Gas Specific Heat Capacity Calculator
A Streamlit web application designed to calculate the mean molar specific heat capacity of ideal gases. It uses linear interpolation on tabulated data to provide precise values between 0°C and a user-specified temperature.

Features
Multi-Gas Support: Calculates specific heat capacity for a wide range of gases including O2, N2, H2, CO2, CH4, and many hydrocarbons.

Linear Interpolation: Algorithmically determines values for temperatures that fall between data points in the provided JSON dataset.

Comparison Tool: Allows users to select and compare results for up to 6 different gases side-by-side.

Interactive UI: Built with Streamlit for a responsive and user-friendly experience.

Project Structure
app.py: The main application script containing the Streamlit UI and interpolation logic.

gasses.json: A JSON database storing specific heat capacity values at various temperature points.

requirements.txt: List of Python dependencies required to run the project.

Installation and Setup
Follow these steps to run the project locally:

Clone the repository:

Bash
git clone https://github.com/TVOJE_KORISNICKO_IME/IME_PROJEKTA.git
cd IME_PROJEKTA
Create a virtual environment:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Usage
To start the application, run the following command in your terminal:

Bash
streamlit run app.py
The application will open automatically in your web browser (usually at http://localhost:8501).

Data Source
The application relies on gasses.json, which must be located in the same directory as app.py. The data is structured with gas names as keys and temperature-value pairs as nested objects.

License
This project is open source.