import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3) / (2*x) - 10*x

x = np.linspace(-5, 5, 100)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of $\\frac{x^3}{2x} - 10x$')
plt.grid()
plt.show()