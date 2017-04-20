#coding: utf-8

from math import pi
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt


#データ数
NUM=1000
x1=np.linspace(0+1/NUM,1-1/NUM,NUM)
x2=np.log(x1/(1-x1))

plt.plot(x1,x2,linewidth=3.0)
plt.xlim((0,1))
plt.ylim((-8,8))
plt.grid()
plt.title("Logit function")
filename="logit_func.png"
plt.savefig(filename)
plt.show()
