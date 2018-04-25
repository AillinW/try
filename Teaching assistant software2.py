# 第二次作业的第二题
# 2018/3/22
# autho：Aillin_W
# 给高中生写一个教学辅助软件，对于三角函数 y=asin(wTheda + fi)，
# 通过键盘输入a, w, fi的值，画出相应的图。
# 要求：可以同时输入多组数据,比如先问学生你需要几组，
# 学生输入后，再输入多组a,w,fi，然后在图中同时用不同的颜色画出。
# python类型转换
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib as mpb
colors_l=tuple(mpb.colors.cnames.keys())#提取颜色列表
n = int(input("请输入组数："))
x = np.linspace(0, 10, 10000)
plt.figure(figsize=(16, 8))
a_max=0;
r=[];
for i in range(n):
    #循环获得参数
    a= float(input("请输入第{}组的a的值:".format(i + 1)))
    if a>a_max:
        a_max=a;
    w =float( input("请输入第{}组的w的值:".format(i + 1)))
    fi= float(input("请输入第{}组的fi的值:".format(i + 1)))
    y = np.sin(x * w+ fi) * a
    #获得随机不同颜色
    while(True):
        temp=int(random.uniform(0, len(colors_l)+1))
        if temp not in r:
            r.append(temp)
            break
    plt.plot(x, y, label="${}*sin({}*x+{})$".format(a,w,fi), color=colors_l[r[i]] , linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Beautiful graphics")
plt.ylim(-1.2*a_max, 1.2*a_max)
plt.legend()
plt.show()
