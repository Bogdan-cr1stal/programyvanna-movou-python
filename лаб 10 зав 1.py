import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 600)

y = 15 * np.sin(10 * x) * np.cos(3 * x)

plt.plot(x, y, label='Y(x) = 15*sin(10x)*cos(3x)', color="blue", linewidth=3)

plt.title('Function graph', fontsize=15)
plt.xlabel('x', fontsize=12, color='red')
plt.ylabel('y', fontsize=12, color='red')
plt.legend()
plt.grid(True)

plt.show()
