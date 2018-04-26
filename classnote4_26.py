# #2018/4/26
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import leastsq
#
# plt.figure(figsize=(9,9))
# x=np.linspace(0,10,1000)
# X=np.array([1.,2.,3.,4.,5.])
# Y=np.array([4,4.5,6,8,8.5])
# def f(p):
#     k,b=p
#     return (Y-(k*X+b))
#
# r=leastsq(f,[1,0])
# k,b=r[0]
# print("k=",k,"b=",b)
#
# plt.scatter(X,Y,s=100,alpha=1.0,marker="o",lable=u"数据点")
# y=k*x+b
# ax=plt


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(9,9))

x = np.linspace(-10,10,1000)

X = np.array([0,1,2,3,-1,-2,-3])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
# X = np.array([-3,-2,-1,0,1,2,3])
# Y = np.array([8.7,3.72,2.21,10.29,3.22,1.85,-1.22])

def f(p):
    a,b,c = p
    return(Y-(a*X*X+b*X+c))

r = leastsq(f, [-5,-5,-5])
a,b,c= r[0]
print("a=",a,"b=",b,"c=",c)

plt.scatter(X,Y, s=100, alpha=1.0, marker='o',label=u'数据点')

y=a*x*x+b*x+c

ax = plt.gca()
# xlim=x.max()*0.1
# ylim=y.max()*0.1
# plt.xlim(x.min()-xlim,x.max()+xlim)
# plt.ylim(y.min()-ylim,y.max()+ylim)

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'拟合曲线')


plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'安培/A')
plt.ylabel(u'伏特/V')

plt.xlim(-10, x.max() * 1.1)
plt.ylim(-2, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()
