
import numpy as np

#Orbit data necessary
d= #distance from the Sun


P=3.856*10^26 #Total power output from the Sun
al_max=0.39
al_min=0.31

#sun radiation
J_s=P/(4*np.pi*d^2)
J_s=1371 #solar intensity mean value for Earth(+-5 W/m^2)

#albedo radiation
J_a=J_s*a*F