import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values
y = (x + 1) / 2 + 5 / x

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\frac{x^{2}+x+10}{2x}$')
plt.title(r'Plot of $\frac{x^{2}+x+10}{2x}$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()