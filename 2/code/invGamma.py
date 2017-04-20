from scipy.stats import invgamma
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from math import pi
from scipy.special import i0

#データ数
NUM=100
a=0.1
"""ガンマ分布"""

fig, ax = plt.subplots(1, 1)
a = 4.07
mean, var, skew, kurt = invgamma.stats(a, moments='mvsk')
x = np.linspace(invgamma.ppf(0.01, a),invgamma.ppf(0.99, a), 100)
ax.plot(x, invgamma.pdf(x, a),'r-', lw=5, alpha=0.6, label='invgamma pdf')
plt.hist(invgamma.rvs(a,NUM), histtype='step', bins=500, range=(0, 10), normed=True)
plt.title("Inv-Gamma dist : Inv-Gam(x|a,b)")
plt.legend(loc="upper right")
filename="invGamma.png"
plt.savefig(filename)
plt.show()