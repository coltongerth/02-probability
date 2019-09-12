import numpy as np

import matplotlib.pyplot as plt

n_genes = 100
n_samples = 100000
mean_height = 170

effects = np.random.rand(n_genes)*10 - 5
heights = []

for n in range(n_samples):
    genes = np.random.randint(0,2,n_genes)
    height_deviation = np.sum(genes*effects)
    heights.append(mean_height + height_deviation)

plt.hist(heights,50)
plt.show()
