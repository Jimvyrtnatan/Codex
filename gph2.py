import matplotlib.pyplot as plt 
import numpy as np

# generate x values 
x = np.linspace(-5, 5, 100)

# calculate y values using the equation
y = x**3 + x - 100

# plot 
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^3 + x - 100$')
plt.title('Plot of $y = x^3 + x - 100$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()