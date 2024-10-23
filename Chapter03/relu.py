import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(x, 0)

X = np.arange(-5, 5, 0.1)
Y = relu(X)
plt.plot(X, Y)
plt.ylim(-1.0, 5.5)
plt.show()