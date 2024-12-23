#Libraries#####################################################################
from Productivity_Scheme import Ridgwell_2007
from Physical_Scheme import Light_attenuation as La
import matplotlib.pyplot as plt
import numpy as np
from alive_progress import alive_bar
from alive_progress import config_handler

config_handler.set_global(length=40, bar = "fish")

#Model Parameters##############################################################
Insolation_local = 1000  # Surface insolation in W/m^2
depths = range(0, 150)   # Depths from 1 to 150 meters

with alive_bar(1) as bar:
    Iz_values = [La.light_attenuation(depth, Insolation_local) for depth in depths]
    bar()

with alive_bar(1) as bar:
    #Biological productivity
    Insolation = np.array(Iz_values) / 1361 #normalises value over water column
    PO4_uptake = Ridgwell_2007.PO4_uptake(PO4_conc=3, Ice_area=0, Insolation = Insolation)
    bar()

plt.figure(figsize=(8, 6))
plt.plot(PO4_uptake, depths,  label="Biological PO4 Uptake", color="blue")
plt.title("Biological Uptake")
plt.ylabel("Depth (m)")
plt.xlabel("PO4 Uptake (umolKg^-1 yr^-1)") #check the units on this...
plt.gca().invert_yaxis()
plt.legend()
plt.show()