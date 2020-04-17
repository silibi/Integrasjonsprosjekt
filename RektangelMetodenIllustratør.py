from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import pylab

# Funksjonen
def f(x):
    return pylab.cos(x)

# Verdier
n = 5
a = 0
b = 1
dx = (b - a)/n

# Lager en subplot (tror jeg?)
plt.figure()
currentAxis = plt.gca()

# Lager rektanglene
for i in range(n):
    currentAxis.add_patch(Rectangle((dx*i, 0), dx, f(dx*i),alpha=1, edgecolor='black'))

# Lager selve funksjonen   
x = pylab.linspace(a, b, 1000)
currentAxis.plot(x, f(x), color='salmon', label='cos(x)')

# Plotting
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('Rektangelmetoden1.png')
plt.show()


    
