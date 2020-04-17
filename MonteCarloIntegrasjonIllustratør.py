import pylab
import random


def f(x):
    return pylab.cos(x)


# Startverdi og Sluttverdi for testfunksjonen
a = 0
b = 1


# Monte Carlo-Integrasjon
N = 10000
for i in range(N):
    x1 = random.uniform(a, b)
    y1 = random.uniform(a, b)
    if y1 <= f(x1):
        pylab.scatter(x1, y1, color='royalblue')
    else:
        pylab.scatter(x1, y1, color='firebrick')


#Lager selve funksjonen
x = pylab.linspace(a, b, 1000)
pylab.plot(x, f(x), color='salmon', label='cos(x)')


pylab.xlabel('x')
pylab.ylabel('y')
pylab.grid()
pylab.legend()
pylab.savefig('MonteCarloIntegrasjon2.png')
pylab.show()