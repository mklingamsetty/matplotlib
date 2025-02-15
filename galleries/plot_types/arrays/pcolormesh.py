"""
===================
pcolormesh(X, Y, Z)
===================
Create a pseudocolor plot with a non-regular rectangular grid.

`~.axes.Axes.pcolormesh` is more flexible than `~.axes.Axes.imshow` in that
the x and y vectors need not be equally spaced (indeed they can be skewed).

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(4, dtype=float)
y = np.linspace(1e1, 1e5, 10)  # all positive
z = np.arange(len(x) * len(y)).reshape(len(x), len(y))

fig, axs = plt.subplots(1, 3, figsize=(9, 3))

# works fine
axs[0].pcolormesh(x, y, z.T)

# potential fix
axs[1].pcolormesh(x, y, z.T)
axs[1].set_ylim(y.min(), y.max())  # Ensure limits are positive
axs[1].set_yscale('log')  

# works fine
axs[2].pcolormesh(x, y, z.T)
axs[2].set_ylim(1e-3, y.max())  # Ensure strictly positive range
axs[2].set_yscale('log')

plt.show()

plt.show()
