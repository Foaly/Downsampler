import numpy as np
import matplotlib.pyplot as plt

changePoint = 2 * np.pi + (np.pi / 2)
sinX = np.linspace(0, changePoint, 200)

# logX = np.logspace(0.01, 1.27, num=50)  # curve
logX = np.logspace(0.01, 1.39, num=50)  # curve 2
logX += changePoint - logX[0]

plt.figure(figsize=[14, 2.5])
plt.plot(sinX, np.sin(sinX), color='black')
plt.step(logX, np.sin(logX), where='post', label='post', color='black')


plt.axis('off')
plt.gca().set_position([0, 0, 1, 1])
plt.gca().set_facecolor('none')

plt.savefig("curve.svg")
plt.show()
