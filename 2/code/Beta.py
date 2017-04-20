#coding: utf-8

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from math import pi
from scipy.special import i0

#データ数
NUM=100000

"""ベータ分布"""
for a in [10,20,40]:
    for b in [10,20]:
        data = list()
        for i in range(NUM):
            data.append(rd.beta(a, b))
        label = "$\\alpha$=%s $\\beta$=%s" %(a, b)
        plt.hist(np.array(data), histtype='step', bins=500, range=(0.0, 1.0), normed=True, label=label)
plt.title("Beta distribution : Beta($\\theta$|$\\alpha$,$\\beta$)")
plt.legend(loc="upper left")
filename="Beta.png"
plt.savefig(filename)
plt.show()
