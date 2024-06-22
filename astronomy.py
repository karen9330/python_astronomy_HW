import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

c = 299792.458  # 光速
H0 = 70  # 哈伯常數
Omega_m = 0.3  # matter density parameter
Omega_Lambda = 0.7  # dark energy density parameter

def H(z):
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + Omega_Lambda)

def luminosity_distance(z):
    integral, _ = quad(lambda z_prime: c / H(z_prime), 0, z)
    return (1 + z) * integral

def angular_diameter_distance(z):
    D_L = luminosity_distance(z)
    return D_L / ((1 + z)**2)

z_values = np.linspace(0, 2, 500)

D_A_values = [angular_diameter_distance(z) for z in z_values]

plt.figure(figsize=(10, 5))
plt.plot(z_values, D_A_values, label='Angular Diameter Distance $D_A(z)$')
plt.title('Angular Diameter Distance as a Function of Redshift')
plt.xlabel('Redshift $z$')
plt.ylabel('Angular Diameter Distance $D_A(z)$ [Mpc]')
plt.grid(True)
plt.legend()
plt.show()

z_max = z_values[np.argmax(D_A_values)]
D_A_max = max(D_A_values)

z_max, D_A_max
