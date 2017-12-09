#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# create x, evenly spaced between 0 to 20
x = np.linspace(0, 20, 1000)

# calculate sin and cos values
y1 = np.sin(x)
y2 = np.cos(x)

# plot the sin and cos functions
plt.plot(x, y1, '-g', label='sine')
plt.plot(x, y2, '-b', label='cos')
# the legend should be in the top right corner
plt.legend(loc='upper right')
# limit the y axis to -1.5 to 1.5
plt.ylim(-1.5, 1.5)
plt.show()
