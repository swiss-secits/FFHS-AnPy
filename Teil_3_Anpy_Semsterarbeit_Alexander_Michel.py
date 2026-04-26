import numpy as np
#import scipy
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Exakte Funktion
def f(x):
    return np.sin(x)

# Fein aufgelöste x-Werte für "exakte" Kurve, Intervall ist 2*np.pi, damit die vollständige Sinuswelle als Intervall definiert ist
x_fine = np.linspace(0, 2*np.pi, 400)
y_exact = f(x_fine)

# 20 Stützstellen (wenige Punkte!), Intervall muss  den Gleich sein
x_nodes = np.linspace(0, 2*np.pi, 20)
y_nodes = f(x_nodes)

# Kubischer Spline
spline = CubicSpline(x_nodes, y_nodes)

# Spline-Auswertung
y_spline = spline(x_fine)

# Plot
plt.figure()
plt.plot(x_fine, y_exact, label="Exakte Kurve (sin(x))")
plt.plot(x_fine, y_spline, '--', label="Spline-Approximation")
plt.scatter(x_nodes, y_nodes, color='red', label="Stützpunkte")

plt.legend()
plt.title("Spline-Approximation von sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()