import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pylab

# Lager en subplot (tror jeg?)
fig, ax = plt.subplots()

# Funksjonen som skal integreres
def f(x):
    return pylab.cos(x)

# Et andregrads polynom som interpolerer i endepunktene og midtpunktet skrevet som et Lagrange polynom
def p2(f, x, ca, cb):
    return (f(ca) * ((x - (ca + cb)/2)/(ca - (ca + cb)/2)) * ((x - cb)/(ca - cb))) + (f((ca + cb)/2) * ((x - ca)/((ca + cb)/2 - ca)) * ((x - cb)/((ca + cb)/2 - cb))) + (f(cb) * ((x - (ca + cb)/2)/(cb - (ca + cb)/2)) * ((x - ca)/(cb - ca)))

# Verdier
n = 10
a, b = 0, 1
dx = (b - a)/n

for i in range(n): 
    ca = a + i*dx
    cb = a + (i + 1)*dx
    ix = np.linspace(ca, cb, 1000)
    iy = p2(f, ix, ca, cb)
    verts = [(ca, 0), *zip(ix, iy), (cb, 0)]
    poly = Polygon(verts, alpha=1, edgecolor='black')
    ax.add_patch(poly)


x = np.linspace(a, b, 1000)
y = f(x)
ax.plot(x, y, color='salmon', label='cos(x)')


# Plotting
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('Simpsonsmetode2.png')
plt.show()
