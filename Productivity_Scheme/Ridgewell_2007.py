def PO4_uptake(PO4_conc = "", Ice_area = "", Insolation = ""):
    """
    PO4_uptake = u_0_PO4 * (PO4/PO4+K^PO4) * (1-A) * I/I_0
    Initial values are based on Ridgewell et al. (2007)
    u_0_PO4 = 1.958 * 10 ** -6
    c0_PO4 = 2.199 * 10 ** -7
    """
    u_0_PO4 = 1.958 * 10 ** -6 #Maximum Nutrient Uptake Rate (mol kg^-1 yr^-1)
    c0_PO4 = 2.199 * 10 ** -7 #PO4 half-saturation value
    uptake = u_0_PO4 * (PO4_conc / (PO4_conc + c0_PO4)) * (1 - Ice_area) * Insolation
    return uptake
