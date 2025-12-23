# 🔬 Gas Specific Heat Capacity Calculator

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern, interactive web application for calculating the mean molar specific heat capacity of ideal gases with precision and ease.

</div>

---

## ✨ Features

- 🌡️ **Multi-Gas Support**: Calculate specific heat capacity for O₂, N₂, H₂, CO₂, CH₄, and numerous hydrocarbons
- 📊 **Linear Interpolation**: Precisely estimate values between data points using advanced algorithms
- 🔄 **Compare & Contrast**: Side-by-side analysis of up to 6 different gases simultaneously
- 💻 **Beautiful UI**: Responsive, intuitive interface powered by Streamlit
- 📈 **Accurate Data**: Comprehensive temperature range with tabulated reference values

---

## 📁 Project Structure

```
AutomaticMolarCalculator/
├── app.py                  # Main Streamlit application
├── gasses.json            # Gas heat capacity database
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AutomaticMolarCalculator.git
   cd AutomaticMolarCalculator
   ```

2. **Create and activate a virtual environment:**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 Usage

Run the application with:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### How to Use
1. Select one or more gases from the dropdown menu
2. Enter the desired temperature value
3. Click calculate to get the mean molar specific heat capacity
4. Compare results across multiple gases in the interactive chart

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Core application logic, UI components, and interpolation algorithms |
| `gasses.json` | Database of gas properties and temperature-dependent heat capacity values |
| `requirements.txt` | Project dependencies and package versions |

---

## 🔧 Technologies Used

- **Streamlit** - Web application framework
- **Python** - Core programming language
- **JSON** - Data storage format
- **NumPy/Pandas** - Data processing (if used)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request.

---

## 📧 Contact

For questions or suggestions, please open an issue in the GitHub repository.

---

<div align="center">

**Made with ❤️ by [Your Name]**

</div>