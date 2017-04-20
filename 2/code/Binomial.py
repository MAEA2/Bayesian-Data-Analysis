#coding: utf-8

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from math import pi
from scipy.special import i0

#データ数
NUM=1000000

"""二項分布分布"""
#パラメータ
for N,theta in [[20,0.5],[30,1/3],[30,2/3],[40,0.5],[50,0.8],[60,2/3]]:
	#データ生成
	x=np.random.binomial(N,theta,NUM)
	plt.hist(x, histtype='step', bins=(N+1), range=(0, N), normed=True)

#プロット
plt.title("Binomial distribution : Bin(y|n,$\\theta$)")
filename="Binomial.png"
plt.savefig(filename)
plt.show()

