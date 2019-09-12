import numpy as np

import matplotlib.pyplot as plt

n_genes = 100
n_samples = 100000
mean_height = 170

effects = np.random.randint(-5,6,n_genes)
heights = []

for n in range(n_samples):
    genes = np.random.randint(0,2,n_genes)
    height_deviation = np.sum(genes*effects)
    heights.append(mean_height + height_deviation)

plt.hist(heights,bins=np.arange(100,250,1))
plt.show()
