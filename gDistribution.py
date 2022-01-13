import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

Wei = np.arange(-90,91,1) #纬度
print(type(Wei))

def gra(a):                #求重力函数
    g = 9.780327*(1+0.00053024*np.sin(a)*np.sin(a)-0.000005*np.sin(2*a)*np.sin(2*a))
    return g
g_late = [ ] #用于存放g的数据

for i in Wei:
    i = i*np.pi/180 #转化为弧度制
    g_late.append(gra(i))
df = pd.DataFrame({'Latitude': Wei,'g (m/s^2)' :g_late})
'''plt.scatter(Wei,g_late)
plt.plot(Wei,g_late)
plt.xlabel('-90S -- 90N')
plt.ylabel('g(m/s^2)')
plt.grid(axis="y")  
plt.show()'''
plt.grid(axis="y")  
sns.regplot( x="Latitude", y="g (m/s^2)",data=df)
plt.title('The distribution of g')
plt.show()


