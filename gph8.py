import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values
y = np.cos(x) / (5 * x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\frac{\cos(x)}{5x}$')
plt.title(r'Plot of $\frac{\cos(x)}{5x}$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()