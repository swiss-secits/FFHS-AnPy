import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# SEKANTENTRAPEZREGEL

def sekanten_trapez_regel(f, a, b, n):

    # Formel um die Höhe zu berechnen
    h = (b - a) / n

    # Erzeugt n+1 Stützstellen zwischen a und b
    # Beispiel:
    # n=4 -> [x0, x1, x2, x3, x4]
    x = np.linspace(a, b, n + 1)

    # Randpunkte zählen nur halb
    # zusammengesetzte Trapezregel
    s = 0.5 * f(x[0]) + 0.5 * f(x[-1])

    # innere Punkte vollständig addieren
    for i in range(1, n):
        s += f(x[i])

    # Multiplikation mit h
    # ergibt die endgültige Approximation
    return h * s

# TANGENTENTRAPEZREGEL

# numerische Ableitung
def ableitung(f, x, eps=1e-6):

    # zentraler Differenzenquotient:
    #
    # f'(x) ≈ (f(x+eps)-f(x-eps)) / (2*eps)
    #
    # eps ist ein sehr kleiner Wert
    return (f(x + eps) - f(x - eps)) / (2 * eps)


def tangenten_trapez_regel(f, a, b, n):

    # Formel um die Höhe zu berechnen
    h = (b - a) / n

    # linke Startpunkte aller Intervalle
    # letzter Punkt ist b-h
    x = np.linspace(a, b - h, n)

    # Summe initialisieren
    s = 0

    # über alle Teilintervalle laufen
    for xi in x:

        # Tangententrapezformel:
        #
        # h/2 * (2f(xi) + f'(xi)*h)
        #
        # f'(xi) wird mit ableitung(...) approximiert
        s += (h / 2) * (2 * f(xi) + ableitung(f, xi) * h)

    return s


# SIMPSONSCHE REGEL

def simpson_regel(f, a, b, n):

    # Formel um die Höhe zu berechnen
    h = (b - a) / n

    # Stützstellen erzeugen
    x = np.linspace(a, b, n + 1)

    # erster + letzter Wert
    s = f(x[0]) + f(x[-1])

    # innere Punkte bearbeiten
    for i in range(1, n):

        # gerade Indizes erhalten Faktor 2
        if i % 2 == 0:
            s += 2 * f(x[i])

        # ungerade Indizes erhalten Faktor 4
        else:
            s += 4 * f(x[i])

    # Endformel der Simpsonregel
    return (h / 3) * s


# FUNKTIONEN DEFINIEREN

# f(x)=1/x
f1 = lambda x: 1/x

# f(x)=x^3+3x^2
f2 = lambda x: x**3 + 3*x**2

# f(x)=cos(x)
f3 = lambda x: np.cos(x)

# EXAKTE WERTE MIT SYMPY BERECHNEN

# symbolische Variable x erzeugen
x = sp.symbols('x')

# exakter Wert Integral 1
ew1 = float(
    sp.integrate(1/x, (x, 1, 2))
)

# exakter Wert Integral 2
ew2 = float(
    sp.integrate(x**3 + 3*x**2, (x, 0, 1))
)

# exakter Wert Integral 3
ew3 = float(
    sp.integrate(
        sp.cos(x),
        (x, -np.pi/2, np.pi/2)
    )
)


# LISTE DER TESTFUNKTIONEN

funktionen = [

    # Name, Funktion, a, b, exakter Wert
    ("1/x", f1, 1, 2, sp.log(2)),

    ("x^3 + 3x^2", f2, 0, 1, sp.Rational(5,4)),

    ("cos(x)", f3, -np.pi/2, np.pi/2, 2)
]


# verschiedene n-Werte
n_werte = [2, 4, 8, 32, 128, 512, 4096]


# über alle Funktionen iterieren
for name, f, a, b, exakt in funktionen:

    print("\nFunktion:", name)

    # Listen für Diagramme
    sekanten = []
    tangenten = []
    simpsons = []


    # verschiedene n testen
    for n in n_werte:

        # Approximationen berechnen
        sekante = sekanten_trapez_regel(f, a, b, n)

        tangente = tangenten_trapez_regel(f, a, b, n)

        simpson = simpson_regel(f, a, b, n)


        # Werte für Diagramm speichern
        sekanten.append(
            sekanten_trapez_regel(f, a, b, n)
        )

        tangenten.append(
            tangenten_trapez_regel(f, a, b, n)
        )

        simpsons.append(
            simpson_regel(f, a, b, n)
        )


        # passenden exakten Wert auswählen
        if f == f1:
            ew = ew1

        elif f == f2:
            ew = ew2

        elif f == f3:
            ew = ew3


        # Ergebnisse + Fehler ausgeben
        print(

            # :.9f bedeutet:
            # Ausgabe mit 9 Nachkommastellen
            f"Sekante={sekante:.9f} "
            f"fehler={abs(sekante - ew):.9f} | "

            f"Tangente={tangente:.9f} "
            f"fehler={abs(tangente - ew):.9f}| "

            f"Simpson={simpson:.9f} "
            f"fehler={abs(simpson - ew):.9f}| "

            f"Exakter Wert={ew}  | "

            f"n={n:2d} "
        )


    # DIAGRAMM ZEICHNEN

    # neues Diagramm erzeugen
    plt.figure(figsize=(8,5))

    # Kurven zeichnen
    plt.plot(
        n_werte,
        sekanten,
        marker="o",
        label="Sekante"
    )

    plt.plot(
        n_werte,
        tangenten,
        marker="o",
        label="Tangente"
    )

    plt.plot(
        n_werte,
        simpsons,
        marker="o",
        label="Simpson"
    )


    # exakten Wert als horizontale Linie zeichnen
    plt.axhline(
        y=float(exakt),
        linestyle="--",
        label="Exakt"
    )

    # Titel des Diagramms
    plt.title(
        f"Approximationen für {name}"
    )

    # Achsenbeschriftungen
    plt.xlabel("n")
    plt.ylabel("Integralwert")

    # Legende anzeigen
    plt.legend()

    # Gitternetz anzeigen
    plt.grid()

    # Diagramm anzeigen
    plt.show()