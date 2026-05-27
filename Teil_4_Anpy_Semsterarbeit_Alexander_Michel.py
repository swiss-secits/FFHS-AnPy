import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Sekantentrapezregel

def sekanten_trapez_regel(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s = 0.5 * f(x[0]) + 0.5 * f(x[-1])
    for i in range(1, n):
        s += f(x[i])

    return h * s

# Tangententrapezregel
def ableitung(f, x, eps=1e-6):
    return (f(x + eps) - f(x - eps)) / (2 * eps)

def tangenten_trapez_regel(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b - h, n)
    s = 0
    for xi in x:
        s += (h / 2) * (2 * f(xi) + ableitung(f, xi) * h)

    return s

# Simpsonsche Regel
def simpson_regel(f, a, b, n):
    # n muss gerade sein
    if n % 2 == 1:
        n += 1

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    s = f(x[0]) + f(x[-1])
    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(x[i])
        else:
            s += 4 * f(x[i])

    return (h / 3) * s

#aufgabe1=sp.integrate(1/x, (x, 1, 2))
#aufgabe2=sp.integrate(x**3 + 3*x**2, (x, 0, 1))
#aufgabe3=sp.integrate(sp.cos(x), (x, sp.pi/2, sp.pi/2))
f1 = lambda x: 1/x
f2 = lambda x: x**3 + 3*x**2
f3 = lambda x: np.cos(x)

x = sp.symbols('x')
ew1 = float(sp.integrate(1/x, (x, 1, 2)))
ew2 = float(sp.integrate(x**3 + 3*x**2, (x, 0, 1)))
ew3 = float(sp.integrate(sp.cos(x), (x, -np.pi/2, np.pi/2)))

funktionen = [
    ("1/x", f1, 1, 2, sp.log(2)),
    ("x^3 + 3x^2", f2, 0, 1, sp.Rational(5,4)),
    ("cos(x)", f3, -np.pi/2, np.pi/2, 2)
]

n_werte = [2, 4, 8, 32, 128, 512, 4096]

for name, f, a, b, exakt in funktionen:

    print("\nFunktion:", name)
    sekanten = []
    tangenten = []
    simpsons = []


    for n in n_werte:

        sekante = sekanten_trapez_regel(f, a, b, n)
        tangente = tangenten_trapez_regel(f, a, b, n)
        simpson = simpson_regel(f, a, b, n)

        sekanten.append(
            sekanten_trapez_regel(f, a, b, n)
        )

        tangenten.append(
            tangenten_trapez_regel(f, a, b, n)
        )

        simpsons.append(
            simpson_regel(f, a, b, n)
        )


        if f == f1:
            ew = ew1
        elif f == f2:
            ew = ew2
        elif f == f3:
            ew = ew3

        print(
            f"Sekante={sekante:.9f} fehler={abs(sekante - ew):.9f} | "
            f"Tangente={tangente:.9f} fehler={abs(tangente - ew):.9f}| "
            f"Simpson={simpson:.9f} fehler={abs(simpson - ew):.9f}| "
            f"Exakter Wert={ew}  | "
            f"n={n:2d} "
        )

    plt.figure(figsize=(8,5))

    plt.plot(n_werte, sekanten, marker="o", label="Sekante")
    plt.plot(n_werte, tangenten, marker="o", label="Tangente")
    plt.plot(n_werte, simpsons, marker="o", label="Simpson")

    # exakter Wert
    plt.axhline(
        y=float(exakt),
        linestyle="--",
        label="Exakt"
    )

    plt.title(f"Approximationen für {name}")

    plt.xlabel("n")
    plt.ylabel("Integralwert")

    plt.legend()
    plt.grid()

    plt.show()