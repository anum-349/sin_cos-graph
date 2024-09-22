import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100) 

sin = np.sin(x)
cos = np.cos(x)

plt.figure(figsize=(15, 9))

plt.plot(x, sin, label='Sine', color='blue')
plt.plot(x, cos, label='Cosine', color='red')

plt.title('Sine and Cosine Functions')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend() 

plt.grid(True)

plt.show()
