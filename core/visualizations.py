import matplotlib.pyplot as plt
import numpy as np

def generate_hs_chart(s_points, h_points):
    fig, ax = plt.subplots()
    ax.plot(s_points, h_points, 'go-', label='Expansion Line')
    ax.set_title("h-s Chart: HTC Steam Cycle")
    ax.set_xlabel("Entropy [J/kg·K]")
    ax.set_ylabel("Enthalpy [J/kg]")
    ax.grid(True)
    return fig

def generate_th_chart(T_exhaust, T_htc):
    fig, ax = plt.subplots()
    # Simplified heat exchange lines
    Q = [0, 100]
    T_hot = [T_exhaust, T_exhaust - 200]
    T_cold = [T_htc - 50, T_htc]
    ax.plot(Q, T_hot, 'r', label='Turbine Exhaust')
    ax.plot(Q, T_cold, 'b', label='HTC Process')
    ax.set_title("T-Ḣ Chart: Heat Recovery")
    ax.set_xlabel("Heat Flow (kW)")
    ax.set_ylabel("Temperature (K)")
    ax.legend()
    return fig