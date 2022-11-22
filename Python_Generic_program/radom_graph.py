import numpy as np
from matplotlib import pyplot as plt

# Generate 100 random data points along 3 dimensions
x, y, scale = (1, 1)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()
