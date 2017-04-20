#coding: utf-8

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from math import pi
from scipy.special import i0

#データ数
NUM=10000000

"""コーシー分布"""
x=rd.standard_cauchy(NUM)
plt.hist(x, histtype='step', bins=1000, range=(-10, 10), normed=True)
plt.title("Standard_Cauchy dist : p(x)")
filename="cauchy.png"
plt.savefig(filename)
plt.show()
