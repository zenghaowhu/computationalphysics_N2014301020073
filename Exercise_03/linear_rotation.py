import os
import time
import math#包含很多数学函数的模块

angle = 0.1#初值有点角度防止转到坐标轴不好计算正切值
delta_angle = (15/180)*math.pi#每次转动角度转化成弧度值
os.system('cls')
while True:
    for n in range(int(math.pi / delta_angle)):
        for i in range(40):
            for j in range(40):
                if math.fabs((j - 20) - math.tan(angle) * (i - 20)) <= 0.5:#判断扫描的点是否在直线上，0.5是精度
                    print('#', end=' ')
                else:
                    print(' ', end=' ')
            print('')
        angle = angle + delta_angle
        time.sleep(0.05)
        k = os.system('cls')


