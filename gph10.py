import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 + x**2 - 2*x - 24

# Generate x values
x = np.linspace(-10, 10, 100)

# Calculate y values
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$(x+2)(x+3)(x-4)$')
plt.title(r'Plot of $(x+2)(x+3)(x-4)$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()