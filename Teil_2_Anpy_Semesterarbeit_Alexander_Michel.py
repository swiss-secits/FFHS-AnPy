# Teil 2 Anpy Semesterarbeit

import numpy as np
import matplotlib.pyplot as plt

#	Funktionsgraphen
# Source: https://matplotlib.org/stable/users/explain/quick_start.html

# x-Werte erzeugen
x = np.linspace(-10, 10, 400)
# Funktion definieren
y = x**2
# Plot erstellen
plt.plot(x, y)
# Beschriftungen
plt.title("Funktionsgraph von f(x) = x^2")
plt.xlabel("x")
plt.ylabel("f(x)")
# Gitter anzeigen
plt.grid()
# Plot anzeigen
plt.show()

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.title("Funktionsgraph von f(x) = sin(x)")
plt.show()

#	Mehrere Funktionsgraphen in der selben Graphik
# x-Werte
x = np.linspace(-5, 5, 2)

# Funktionen
y1 = x**2
y2 = np.sin(x)
y3 = x*3+2

# Graphen zeichnen
plt.plot(x, y1, label="f(x) = x^2")
plt.plot(x, y2, label="g(x) = sin(x)")
plt.plot(x, y3, label="h(x) = 3x + 2")

# Beschriftungen
plt.title("Mehrere Funktionsgraphen")
plt.xlabel("x")
plt.ylabel("y")

# Legende und Gitter
plt.legend()
plt.grid()

# Anzeigen
plt.show()


#	Balkendiagramme
# Source Code: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html
# Beispiel von Source Code direkt implementiert ohne Anpassungen
species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()

# Eigenes Beispiel
x = [1,2,3,4,5]
y = [1,4,9,16,25]

# plt.bar funktion für Balkendiagramme
plt.bar(x, y)
plt.title("Balkendiagramm f(x)=x^2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

#	Tortendiagramme
# Source Code: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
# Beispiel von Source Code direkt implementiert ohne Anpassungen
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()
data = 0
fig = 0

#Eigenes Beispiel:
# Source Code: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
# Label pro Wert angeben
labels = 'Hunde', 'Katzen', 'Schildkröten', 'Hasen'
# Werte definieren
sizes = [2, 7, 4, 3]

fig, ax = plt.subplots()
plt.title('Verhältnis der Anzahl Tiere in der Familie', fontsize=20)
# Kuchendiagramm mit label und prozenzahl darstellen erstellen
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

#	Histogramme
# Source Code: https://matplotlib.org/stable/gallery/animation/animated_histogram.html
# Beispiel von Source Code direkt implementiert ohne Anpassungen (nur die Speicherung als HTML wurde hinzugefügt)
import functools

import matplotlib.animation as animation
# Setting up a random number generator with a fixed state for reproducibility.
rng = np.random.default_rng(seed=19680801)
# Fixing bin edges.
HIST_BINS = np.linspace(-4, 4, 100)

# Histogram our data with numpy.
data = rng.standard_normal(1000)
n, _ = np.histogram(data, HIST_BINS)

def animate(frame_number, bar_container):
    data = rng.standard_normal(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)

    return bar_container.patches

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

anim = functools.partial(animate, bar_container=bar_container)
ani = animation.FuncAnimation(fig, anim, 50, repeat=False, blit=True)
plt.show()
#Wird kein Show gemacht, es wird eine HTML Datei erzeugt

# Da die PNG Grafik nicht animierte Werte darstellen kann, wird der Output als HTML Datei gespeichert
htmlanimation = animation.Animation.to_jshtml(ani)
with open("htmlanimation-histogram.html", "a") as f:
    f.write(htmlanimation)


# Eigenes Beispiel
# Source Code Quelle: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
# x-Werte (viele Punkte für gute Verteilung)
# Beispiel-Daten: Anzahl Cyberangriffe pro Tag
daten = [
    "2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02",
    "2026-03-02", "2026-03-03", "2026-03-03", "2026-03-04",
    "2026-03-05", "2026-03-05", "2026-03-06"
]

# Histogramm erstellen via plt.hist Funktion. Die Anzahl Datum wiederholungen sind die Anzahl Angriffe an diesem Tag, sprich die plt.hist Funktion behinhaltet standard mässig eine count funktion.
plt.hist(daten, bins=20)

# Beschriftung
plt.title("Verteilung Cyberangriffe pro Tag (Schweiz)")
plt.xlabel("Anzahl Angriffe pro Tag")
plt.ylabel("Häufigkeit")

plt.grid()
plt.show()