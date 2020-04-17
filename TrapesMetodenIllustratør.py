import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pylab

# Funksjonen
def f(x):
    return pylab.cos(x)

# Verdier
n = 100
a = 0
b = 1
dx = (b - a)/n

# Lager en subplot (tror jeg?)
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')


# Trapesene
for i in range(n):
    x = [i * dx, (i + 1) * dx, (i + 1) * dx, i * dx]
    y = [0, 0, f((i + 1) * dx), f(i * dx)]
    ax.add_patch(patches.Polygon(xy=list(zip(x,y)), alpha = 1, edgecolor='black'))
    
#Lager selve funksjonen
x = pylab.linspace(a, b, 1000)
ax.plot(x, f(x), color='salmon', label='cos(x)')

# Plotting
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('Trapesmetoden2.png')
plt.show() 