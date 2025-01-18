import numpy as np
import matplotlib.pyplot as plt

from junk.utils import set_configuration


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-5, 5, 100)
y = [sigmoid(v) for v in x]

# plt.figure(figsize=(15, 10))
plt.plot(x, y, label=r'$s(x) = \frac{1}{1 + e^{-x}}$', linewidth=3)
plt.axhline(0, -10, 10, color='black', linewidth=3)
plt.axvline(0, -1, 1, color='black', linewidth=3)
plt.xlim(-5, 5)
set_configuration('$x$', '$y$')
plt.savefig('./plots/sigmoid.png')