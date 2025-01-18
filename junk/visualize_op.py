import numpy as np
import matplotlib.pyplot as plt

from junk.utils import set_configuration


def op(x):
    return abs(0.5 - x) * 2


x = np.linspace(0, 1, 100)
y = [op(v) for v in x]

# plt.figure(figsize=(15, 10))
plt.plot(x, y, label=r'$op(x) = 2|0.5 - x|$', linewidth=3)
plt.axhline(0, -10, 10, color='black', linewidth=3)
plt.axvline(0, -1, 1, color='black', linewidth=3)
plt.xlim(-0.1, 1.1)
set_configuration('$x$', '$y$')
plt.savefig('./plots/op.png')