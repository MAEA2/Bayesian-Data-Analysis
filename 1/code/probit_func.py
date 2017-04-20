#coding: utf-8

from math import pi
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt


#データ数
NUM=1000
x1=np.linspace(-5,5,NUM)

#標準正規分布
x2=np.exp(-x1**2/2)/np.sqrt(2*pi)

plt.plot(x1,x2,linewidth=3.0)
plt.xlim((-5,5))
plt.ylim((0,0.5))
plt.grid()
plt.title("standard normal distribution : N(x|0,1)")
filename="sn.png"
plt.savefig(filename)
plt.show()


#正規累積分布関数
x3=np.zeros(NUM)
for i in range(NUM):
	x3[i]=np.sum(x2[:i])
x3/=x3[NUM-1]

plt.plot(x1,x3,linewidth=3.0)
plt.xlim((-5,5))
plt.ylim((0,1))
plt.grid()
plt.title("standard normal cumulative distribution function : $\\Phi$")
filename="sn_cdf.png"
plt.savefig(filename)
plt.show()


#プロビット関数
x4=np.linspace(0,1,NUM)
x5=np.zeros(NUM)
for i in range(NUM):
	temp=abs(x3[i]-x4)
	x5[i]=x1[np.argmin(temp)]

plt.plot(x4,x5,linewidth=3.0)
plt.xlim((-0,1))
plt.ylim((-6,6))
plt.grid()
plt.title("Probit function : $\\Phi^{-1}$")
filename="probit_func.png"
plt.savefig(filename)
plt.show()
