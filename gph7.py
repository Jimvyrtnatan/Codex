import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values
y = x**3 + 2*x**2 - 10*x + 3

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$x^{3}+2x^{2}-10x+3$')
plt.title(r'Plot of $x^{3}+2x^{2}-10x+3$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()