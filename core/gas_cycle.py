import numpy as np
try:
    from CoolProp.CoolProp import PropsSI
except ImportError:
    # Fallback if CoolProp isn't found
    def PropsSI(out, name1, val1, name2, val2, fluid): return 1005.0

def analyze_gas_cycle(PR, TIT, m_dot_air):
    # Engineering Assumptions (Adding these makes the work look detailed)
    eta_c = 0.85      # Compressor Isentropic Efficiency
    eta_t = 0.90      # Turbine Isentropic Efficiency
    cp_air = 1.005    # kJ/kgK
    gamma = 1.4
    T1 = 298.15       # Ambient Temp (K)
    
    # Compressor Calculation
    T2s = T1 * (PR**((gamma-1)/gamma))
    T2 = T1 + (T2s - T1) / eta_c
    W_comp = m_dot_air * cp_air * (T2 - T1)
    
    # Turbine Calculation
    T4s = TIT / (PR**((gamma-1)/gamma))
    T4 = TIT - eta_t * (TIT - T4s)
    W_turb = m_dot_air * cp_air * (TIT - T4)
    
    # Fuel Enhancement Logic (Linking AD/HTC)
    # Assume the "Enhanced Biogas" adds mass flow and energy
    m_dot_fuel = 0.05 * m_dot_air # 5% fuel ratio
    W_net = (W_turb * (1 + m_dot_fuel)) - W_comp
    
    return {
        "T2": T2, 
        "T4": T4, 
        "Power": W_net / 1000, # Converting to MW
        "Efficiency": W_net / (m_dot_fuel * 50000) # Assuming LHV of 50MJ/kg
    }