Synthesizing 10/10 solutions

=======
Suggestion 1

def get_new_coordinate(x, y, d):
    import math
    rad = d * math.pi / 180
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)
    return new_x, new_y

=======
Suggestion 2

def problem259_b():
    a,b,d = input().split(' ')
    a = float(a)
    b = float(b)
    d = float(d)
    import math
    d = math.radians(d)
    a1 = a * math.cos(d) - b * math.sin(d)
    b1 = a * math.sin(d) + b * math.cos(d)
    print('{0:.20f} {1:.20f}'.format(a1,b1))

=======
Suggestion 3

def rotate(x, y, d):
    import math
    d = math.radians(d)
    x2 = x * math.cos(d) - y * math.sin(d)
    y2 = x * math.sin(d) + y * math.cos(d)
    return x2, y2

a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

=======
Suggestion 4

def rotate(x, y, d):
    import math
    pi = math.pi
    r = d * pi / 180
    x1 = x * math.cos(r) - y * math.sin(r)
    y1 = x * math.sin(r) + y * math.cos(r)
    return x1, y1

=======
Suggestion 5

def rotate(x, y, d):
    import math
    rad = math.radians(d)
    x1 = x * math.cos(rad) - y * math.sin(rad)
    y1 = x * math.sin(rad) + y * math.cos(rad)
    return x1, y1

=======
Suggestion 6

def main():
    a, b, d = map(int, input().split())
    import math
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x, y)

=======
Suggestion 7

def rotate(a,b,d):
    import math
    d=math.radians(d)
    a_=a*math.cos(d)-b*math.sin(d)
    b_=a*math.sin(d)+b*math.cos(d)
    return a_,b_
a,b,d=map(float,input().split())
a_,b_=rotate(a,b,d)
print(a_,b_)

=======
Suggestion 8

def rotate(x, y, d):
    import math
    x2 = x * math.cos(math.radians(d)) - y * math.sin(math.radians(d))
    y2 = x * math.sin(math.radians(d)) + y * math.cos(math.radians(d))
    return x2, y2

=======
Suggestion 9

def rotate(a, b, d):
    import math
    theta = math.radians(d)
    a_ = a * math.cos(theta) - b * math.sin(theta)
    b_ = a * math.sin(theta) + b * math.cos(theta)
    return a_, b_

=======
Suggestion 10

def rotate(a,b,d):
    import math
    # 将角度转换为弧度
    d = math.radians(d)
    # 计算新的x坐标
    x = a * math.cos(d) - b * math.sin(d)
    # 计算新的y坐标
    y = a * math.sin(d) + b * math.cos(d)
    return x,y
