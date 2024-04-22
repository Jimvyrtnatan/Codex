import matplotlib.pyplot as plt 
import numpy as np

# generate x values 
x = np.linspace(-5, 5, 100)

# calculate y values using the equation
y = x**18 - x**8 + x**2 - 8

# plot 
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^18 - x^8  + x^2  - 8$')
plt.title('Plot of $y = x^18 - x^8  + x^2  - 8$')
plt.xlabel('x', color='b')
plt.ylabel('y', color='w')
plt.grid(True)
plt.legend()
plt.show()