import math

# Function to calculate light attenuation
def light_attenuation(depth, Insolation_local):
    """
    Calculate light attenuation at a given depth.
    Uses the formula: I(z) = I_0 * e^(-k*z)
    Currently taking Kd to be 0.15 based on Yang et al. (2023)
    DOI: 10.1109/ICRA48891.2023.10161047
    """
    k = 0.15  # Attenuation coefficient
    return Insolation_local * math.exp(-k * depth)


