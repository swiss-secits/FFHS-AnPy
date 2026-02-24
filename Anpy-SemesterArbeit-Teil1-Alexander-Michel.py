# Aufgabe 1. (Implementieren Sie eine Python-Funktion fib(n), die die n-te Fibonacci-Zahl bestimmt. Für n >= 2)
def fib(n):
    if n <= 2:
      f = 1
    else:
      f = n-1+n-2
    return f

print(fib(7))

# Aufgabe 2. (Eine naive Implementierung setzt die obige Rekursionsgleichung direkt um. Schreiben Sie eine weitere Python-Funktion, die berechnet, wie viele Funktionsaufrufe on fib notwendig sind, um die n-te Fibonacci-Zahl zu berechnen.)
aufrufe = [0]
def fib_aufrufe(n):
    global aufrufe
    aufrufe[0] += 1
    if n==1:
      f = 1
    elif n==2:
      f = 1
    else:
      f = fib_aufrufe(n-1)+fib_aufrufe(n-2)
    return f

print(fib_aufrufe(5), aufrufe)
print(fib_aufrufe(7), aufrufe)
print(fib_aufrufe(8), aufrufe)

# Aufgabe 3. (Vergleichen Sie die Anzahl der Funktionsaufrufe von fib zur Bestimmung einer Fibonacci-Zahl mit den Fibonacci-Zahlen selber. Können Sie eine Vermutung aufstellen?)
import time
te =  0
aufrufe = 0
aufrufe_liste = [0]

def fib_aufrufe_graph(n):
    global aufrufe, te
    tr = time.time()
    aufrufe += 1
    if n <= 2:
      f = 1
    else:
      f = fib_aufrufe_graph(n-1)+fib_aufrufe_graph(n-2)
    te = time.time()-tr
    return f

print(fib_aufrufe_graph(2), " 2")
aufrufe2 = aufrufe
Dauer2 = te
print(fib_aufrufe_graph(3), " 3")
aufrufe3 = aufrufe
Dauer3 = te
print(fib_aufrufe_graph(4))
aufrufe4 = aufrufe
Dauer4 = te
print(fib_aufrufe_graph(5))
aufrufe5 = aufrufe
Dauer5 = te
print(fib_aufrufe_graph(6))
aufrufe6 = aufrufe
Dauer6 = te
print(fib_aufrufe_graph(7))
aufrufe7 = aufrufe
Dauer7 = te

import matplotlib.pyplot as plt

#Anzahl aufrufe mit Fibonaccizahl vergleichen
xiterativewerte=[1, 2, 3, 5, 8, 13]
yiterativewerte= [aufrufe2, aufrufe3, aufrufe4, aufrufe5, aufrufe6, aufrufe7]

#plt.bar(xiterativewerte, yiterativewerte)
plt.plot(xiterativewerte, yiterativewerte)
plt.scatter(xiterativewerte, yiterativewerte)

plt.ylabel("Anzahl rekursive Funktionsaufrufe")
plt.xlabel("fibonacci Zahl ")
plt.show()

# Aufgabe 4. (Verwenden Sie die Funktion time() aus dem Modul time, um zu bestimmen, wie lange die Funktion fib benötigt, um eine Fibonacci-Zahl zu bestimmen.)
te =  0
def fib(n):
    global te
    tr = time.time()
    if n < 2:
        return n
    p = fib(n-1)+fib(n-2)
    te = time.time()-tr
    return p

#Dauer der Berechung mit berechneter Fibonaccizahl vergleichen
xiterativewerte=[1, 2, 3, 5, 8, 13]
yiterativewerte= [Dauer2, Dauer3, Dauer4, Dauer5, Dauer6, Dauer7]

plt.plot(xiterativewerte, yiterativewerte)
plt.scatter(xiterativewerte, yiterativewerte)

plt.ylabel("Berechungsdauer der rekursiven Funktion")
plt.xlabel("fibonacci Zahl")
plt.show()

# Aufgabe 5. (Implementieren Sie eine weitere Python-Funktion zur Berechnung der n-ten Fibonacci-Zahl, die möglichst effizient ist. (Hinweis: das kann rekursiv oder iterativ gelöst werden.))

# Iterative Fibonacci-Funktion
count = 0
te = 0
def fib_interativ(n):
    global count, te
    count = count + 1
    ti = time.time()
    a,b=0,1
    for i in range(n):
        a, b = b, a + b
    te = time.time() - ti
    return a

print(fib_interativ(2), " 2")
aufrufe2 = count
Dauer2 = te
print(fib_interativ(3), " 3")
aufrufe3 = count
Dauer3 = te
print(fib_interativ(4))
aufrufe4 = count
Dauer4 = te
print(fib_interativ(5))
aufrufe5 = count
Dauer5 = te
print(fib_interativ(6))
aufrufe6 = count
Dauer6 = te
print(fib_interativ(7))
aufrufe7 = count
Dauer7 = te

#Anzahl aufrufe mit Fibonaccizahl vergleichen
xiterativewerte=[1, 2, 3, 5, 8, 13]
yiterativewerte= [aufrufe2, aufrufe3, aufrufe4, aufrufe5, aufrufe6, aufrufe7]

plt.plot(xiterativewerte, yiterativewerte)
plt.scatter(xiterativewerte, yiterativewerte)

plt.ylabel("Anzahl iterative Funktionsaufrufe")
plt.xlabel("fibonacci Zahl ")
plt.show()

#Dauer der Berechung mit berechneter Fibonaccizahl vergleichen
xiterativewerte=[1, 2, 3, 5, 8, 13]
yiterativewerte= [Dauer2, Dauer3, Dauer4, Dauer5, Dauer6, Dauer7]

plt.plot(xiterativewerte, yiterativewerte)
plt.scatter(xiterativewerte, yiterativewerte)

plt.ylabel("Berechungsdauer der iterativen Funktion")
plt.xlabel("fibonacci Zahl ")
plt.show()