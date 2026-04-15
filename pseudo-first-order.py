import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


time = np.array([0, 10, 20, 30, 40, 50, 60])

# Here different experimntal photocatalytic degradation percentages can be used that are associated with experimental reaction. It can be simply calculated in Excel, via noticing the position of curves at their maximum wavelength. In most suc degradation cases, the curve slowlwly flattens out showing degradation. This fall in values/ degradation percentage is exactly what has been used here. 

degradation = np.array([0, 12, 27, 39, 48, 60, 68])
#the increasing values show an increase in the C0/C fraction since as degradation occurs c decreases leading to a much smaller C/C0 value while showing an incresing trend in C0/C fraction

#Photocatalytic degradation definition:
#%Degradation = (C0 - C) / C0 × 100, so, 
#C/C0 = 1 - (%Degradation / 100)
#So, it can be simply calculated via the absorption or concentration as according to Beer-Lamber's Law: A=e*c*l
C = 1 - degradation / 100
C = np.clip(C, 1e-6, None)

# Pseudo 1st Order Kinetics (Only first order of whole Langmuir-Hinshelwood kinetic model has been used here)
ln_C0_C = np.log(1 / C)

# Linear Regressio;n
slope, intercept, r_value, p_value, std_err = linregress(time, ln_C0_C)
k_app = slope
R2 = r_value**2

# ine Fitting
fit_line = intercept + slope * time

# Plotting:
plt.figure(figsize=(8,5))

plt.scatter(time, ln_C0_C, color='blue', label='Experimental data')
plt.plot(time, fit_line, color='red', label='Linear fit')

# Labesls of axes: 
plt.xlabel("Time (min)")
plt.ylabel("ln(C0/C)")
plt.title("Pseudo-First Order Kinetics Analysis")

# Evaluated K_app and R^2 values
text = f"""k_app = {k_app:.4f} min⁻¹
R² = {R2:.4f}"""

plt.text(
    0.05, 0.75,
    text,
    transform=plt.gca().transAxes,
    fontsize=11,
    bbox=dict(facecolor='white', alpha=0.7)
)

plt.legend()
plt.grid(True)
plt.show()

# Printed Value box: 
print("k_app =", k_app)
print("R^2 =", R2)
