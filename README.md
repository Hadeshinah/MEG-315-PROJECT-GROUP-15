# AD-HTC Fuel-Enhanced Gas Power Cycle

This repository contains a comprehensive simulation and UI/UX interface for an integrated Anaerobic Digestion (AD) and Hydrothermal Carbonization (HTC) Power Cycle.

## Features
- **Interactive UI:** Built with Streamlit, integrating input parameters directly into the cycle schematics.
- **Thermodynamic Engine:** Powered by `CoolProp` for high-accuracy state property calculations.
- **Visual Analysis:** - **h-s Chart:** Visualizing the HTC Steam Cycle expansion.
  - **T-Ḣ Chart:** Mapping the heat exchange between turbine exhaust and the HTC process.

## Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `streamlit run app/main.py`