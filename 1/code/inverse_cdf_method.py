#coding: utf-8

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

NUM=10000
#確率分布関数
x1=np.linspace(-2,2,NUM)
x2=3/16*x1*x1

plt.plot(x1,x2,linewidth=3.0)
plt.xlim((-2.2,2.2))
plt.ylim((0,1))
plt.grid()
plt.title("probability function : $p(x)=\\frac{3}{16}x^2 (-2\\leq x \\leq 2)$")
filename="pf.png"
plt.savefig(filename)
plt.show()


#累積確率分布関数
x3=1/16*(x1*x1*x1+8)

plt.plot(x1,x3,linewidth=3.0)
plt.xlim((-2.2,2.2))
plt.ylim((0,1))
plt.grid()
plt.title("cumulative distribution function : $P(x)=\\frac{1}{16}(x^3+8) (-2\\leq x \\leq 2)$")
filename="cdf.png"
plt.savefig(filename)
plt.show()



#逆cdf法
x4=rd.rand(NUM)
x5=np.zeros(NUM)

for i in range(NUM):
	temp=abs(x4[i]-x3)
	x5[i]=x1[np.argmin(temp)]

plt.xlim((-2.2,2.2))
plt.ylim((0,1))
plt.grid()
plt.hist(x5,histtype="step",bins=100,linewidth=3.0,normed=True)
plt.title("inverse cdf method : $p(x)=\\frac{3}{16}x^2 (-2\\leq x \\leq 2)$")
filename="inverse_cdf.png"
plt.savefig(filename)
plt.show()
