import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 100)

# Calculate y values
y = np.sin(x) / (3 * x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\frac{\sin(x)}{3x}$')
plt.title(r'Plot of $\frac{\sin(x)}{3x}$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()