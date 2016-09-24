import os
import time

#6*6字母点阵
a = ['  ##  ',' #  # ','#    #','######','#    #','#    #']
b = ['##### ','#    #','##### ','#    #','#    #','##### ']
c = [' #### ','#    #','#     ','#     ','#    #',' #### ']
d = ['##### ','#    #','#    #','#    #','#    #','##### ']
e = ['######','#     ','##### ','#     ','#     ','######']
f = ['######','#     ','##### ','#     ','#     ','#     ']
g = [' #### ','#    #','#     ','#  ###','#    #',' #### ']
h = ['#    #','#    #','######','#    #','#    #','#    #']
i = ['   #  ','   #  ','   #  ','   #  ','   #  ','   #  ']
j = ['     #','     #','     #','     #','#    #',' #### ']
k = ['#    #','#   # ','####  ','#  #  ','#   # ','#    #']
l = ['#     ','#     ','#     ','#     ','#     ','######']
m = ['#    #','##  ##','# ## #','#    #','#    #','#    #']
n = ['#    #','##   #','# #  #','#  # #','#   ##','#    #']
o = [' #### ','#    #','#    #','#    #','#    #',' #### ']
p = ['##### ','#    #','#    #','##### ','#     ','#     ']
q = [' #### ','#    #','#    #','#  # #','#   # ',' ### #']
r = ['##### ','#    #','#    #','##### ','#   # ','#    #']
s = [' #### ','#     ',' #### ','     #','#    #',' #### ']
t = [' #####','   #  ','   #  ','   #  ','   #  ','   #  ']
u = ['#    #','#    #','#    #','#    #','#    #',' #### ']
v = ['#    #','#    #','#    #','#    #',' #  # ','  ##  ']
w = ['#    #','#    #','#    #','# ## #','##  ##','#    #']
x = ['#    #',' #  # ','  ##  ','  ##  ',' #  # ','#    #']
y = [' #   #','  # # ','   #  ','   #  ','   #  ','   #  ']
z = ['######','    # ','   #  ','  #   ',' #    ','######']

table = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] #字母表

str = input("What's your name:\n")#读取你的名字
name = str.upper()#把字母转换为大写

i = os.system('cls')

def move_str(string):
    for i in range(50):
        for n1 in range(6):  # 每个要显示的字符串有6行
            for j in range(i):    #输出空格
                print(' ',end='')
            for char in string:  # 遍历字符串每个字母
                index = ord(char) - 65
                print(table[index][n1], end=' ')  # 按上面给出的字模点阵打印每一行
            print('')

        time.sleep(0.05)    #延时形成视觉残留,对于我这样的低配置电脑，其实不加运行也会自动延时
        i = os.system('cls')#清屏刷新显示
move_str(name)
