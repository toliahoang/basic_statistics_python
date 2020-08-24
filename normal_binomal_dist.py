import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean =np.mean(sunflowers)
sunflowers_std=np.std(sunflowers)
print(sunflowers_mean)
print(sunflowers_std)
# Calculate sunflowers_normal here:
sunflowers_normal=np.random.normal(13.00215,1.123,5000)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()

# Calculate probabilities here:
experiments=np.random.binomial(200,0.1,5000)
prob=np.mean(experiments < 20)

print(prob)
