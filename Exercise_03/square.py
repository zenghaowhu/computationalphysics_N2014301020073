import os
import time

while True:
    for n in range(10):     #放大
        for i in range(20):
            for j in range(20):
                if (i >= 10 - n and i <= 10 + n)and(j >= 10 - n and j <= 10 + n):#在矩形区域就打印字符
                    print("#",end=' ')
                else:
                    print(' ',end=' ')#不在矩形区域打印空格
            print('')
        time.sleep(0.05)
        k = os.system('cls')
    for n in range(10,0,-1): #缩小
        for i in range(20):
            for j in range(20):
                if (i >= 10 - n and i <= 10 + n)and(j >= 10 - n and j <= 10 + n):
                    print("#",end=' ')
                else:
                    print(' ',end=' ')
            print('')
        time.sleep(0.05)
        k = os.system('cls')