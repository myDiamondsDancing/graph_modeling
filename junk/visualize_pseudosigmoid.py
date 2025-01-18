import numpy as np
import matplotlib.pyplot as plt

from junk.utils import pseudo_sigmoid, set_configuration

x = np.linspace(0, 1, 100)
y = [pseudo_sigmoid(v) for v in x]

# plt.figure(figsize=(15, 10))
plt.plot(x, y, label='$ps(x)$', linewidth=3)
plt.axhline(0, -10, 10, color='black', linewidth=3)
plt.axvline(0, -1, 1, color='black', linewidth=3)
set_configuration('$x$', '$y$')
plt.savefig('./plots/pseudo_sigmoid.png')