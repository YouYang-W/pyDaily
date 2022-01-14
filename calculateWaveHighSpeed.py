'''
author: YouYang
date: 2021/9/12
factor:给定水深和周期计算波长
'''
import math
x = 0.01      #x代表误差限
pi = math.pi   #pi的值
h = eval(input("输入水深：") )
T = eval(input("输入周期：") )       #h是水深，本题h取20或600，计算不同水深时候自己修改
a = 4*pi*pi  / (T*T) #a代表是公式左边

#做一个带小数的循环
for i in range(1,10000):
    for j in range(0,10):       
        for k in range(0,10):
            L = i + 0.1 * j + 0.01 * k
        if abs( a-9.8*( 2*pi/L ) * math.tanh( 2*pi*h/L ) ) < x: #这里代表公式左侧-右侧小于某个误差限
            print( round(L,2))
        

