#coding: utf-8

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from math import pi
from scipy.special import i0

#データ数
NUM=100000

"""ガンマ分布"""
for a in [1.0,2.0,4.0]:
    for b in [1.0,2.0]:
        data = list()
        for i in range(NUM):
            data.append(rd.gamma(a, b))
        label = "a=%s b=%s" %(a, b)
        plt.hist(np.array(data), histtype='step', bins=500, range=(0, 10), normed=True, label=label)
plt.title("Gamma dist : Gam(x|a,b)")
plt.legend(loc="upper right")
filename="Gamma.png"
plt.savefig(filename)
plt.show()
