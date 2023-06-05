Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate(a,b,d):
    import math
    d = math.radians(d)
    import numpy as np
    x = np.array([[math.cos(d),-math.sin(d)],[math.sin(d),math.cos(d)]])
    y = np.array([a,b])
    z = np.dot(x,y)
    return z

print(rotate(-505,191,278))

=======
Suggestion 2

def rotate_point(x, y, d):
    # x, y 是点的坐标
    # d 是旋转角度
    import math
    rad = math.radians(d)
    x1 = x * math.cos(rad) - y * math.sin(rad)
    y1 = x * math.sin(rad) + y * math.cos(rad)
    return x1, y1

=======
Suggestion 3

def rotation(a,b,d):
    import math
    a1 = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
    b1 = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))
    return a1,b1

=======
Suggestion 4

def rotate(a,b,d):
    import math
    pi = math.pi
    d = d*pi/180
    a1 = a*math.cos(d) - b*math.sin(d)
    b1 = a*math.sin(d) + b*math.cos(d)
    return a1,b1

a,b,d = map(int,input().split())
a1,b1 = rotate(a,b,d)
print(a1,b1)

=======
Suggestion 5

def rotate(x, y, d):
    import math
    x1 = x*math.cos(math.radians(d)) - y*math.sin(math.radians(d))
    y1 = x*math.sin(math.radians(d)) + y*math.cos(math.radians(d))
    return x1, y1

x, y, d = map(int, input().split())
x1, y1 = rotate(x, y, d)
print(x1, y1)

=======
Suggestion 6

def main():
    # 读取输入
    x, y, d = map(int, input().split())
    # 计算
    # 旋转矩阵
    # x' = x * cos(d) - y * sin(d)
    # y' = x * sin(d) + y * cos(d)
    x1 = x * math.cos(math.radians(d)) - y * math.sin(math.radians(d))
    y1 = x * math.sin(math.radians(d)) + y * math.cos(math.radians(d))
    # 输出
    print(x1, y1)

=======
Suggestion 7

def problems259_b(a, b, d):
    import math
    d = math.radians(d)
    a1 = a * math.cos(d) - b * math.sin(d)
    b1 = a * math.sin(d) + b * math.cos(d)
    return a1, b1

=======
Suggestion 8

def rotate(x,y,d):
    import math
    d = math.radians(d)
    x_ = x*math.cos(d) - y*math.sin(d)
    y_ = x*math.sin(d) + y*math.cos(d)
    return x_,y_

=======
Suggestion 9

def problems259_b():
    pass

=======
Suggestion 10

def rota(a,b,d):
    import math
    d1 = math.radians(d)
    x = a * math.cos(d1) - b * math.sin(d1)
    y = a * math.sin(d1) + b * math.cos(d1)
    return x,y

a,b,d = map(int,input().split())
x,y = rota(a,b,d)
print(x,y)
