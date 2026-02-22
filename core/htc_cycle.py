from CoolProp.CoolProp import PropsSI

def get_steam_state(P_bar, T_celsius):
    P = P_bar * 1e5  # Convert to Pa
    T = T_celsius + 273.15 # Convert to K
    
    try:
        h = PropsSI('H', 'P', P, 'T', T, 'Water')
        s = PropsSI('S', 'P', P, 'T', T, 'Water')
        return h, s
    except:
        return 0, 0