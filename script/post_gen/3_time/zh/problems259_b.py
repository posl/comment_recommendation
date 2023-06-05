Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def rotate(a, b, d):
    import math
    d = math.radians(d)
    a_ = a*math.cos(d)-b*math.sin(d)
    b_ = a*math.sin(d)+b*math.cos(d)
    return a_, b_

=======
Suggestion 2

def rotate(a, b, d):
    import math
    x = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
    y = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
    return x, y

=======
Suggestion 3

def rotate_point(a,b,d):
    import math
    d = math.radians(d)
    a_new = a*math.cos(d) - b*math.sin(d)
    b_new = a*math.sin(d) + b*math.cos(d)
    return a_new,b_new

=======
Suggestion 4

def problems259_b():
    pass

=======
Suggestion 5

def rotate(x, y, d):
    import math
    rad = math.radians(d)
    x_1 = x * math.cos(rad) - y * math.sin(rad)
    y_1 = x * math.sin(rad) + y * math.cos(rad)
    return x_1, y_1

=======
Suggestion 6

def rotatePoint(x, y, d):
    import math
    #math.pi为圆周率
    d = math.radians(d)
    x1 = x * math.cos(d) - y * math.sin(d)
    y1 = x * math.sin(d) + y * math.cos(d)
    return x1, y1

a, b, d = map(int, input().split())
x, y = rotatePoint(a, b, d)
print(x, y)

=======
Suggestion 7

def rotate(a,b,d):
    import math
    d = math.radians(d)
    a_ = a * math.cos(d) - b * math.sin(d)
    b_ = a * math.sin(d) + b * math.cos(d)
    return a_,b_

a,b,d = map(int,input().split())
a_,b_ = rotate(a,b,d)
print(a_,b_)

=======
Suggestion 8

def rotate(x, y, d):
    import math
    rad = math.radians(d)
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)
    return new_x, new_y

=======
Suggestion 9

def rotate(a,b,d):
    import math
    a1=a*math.cos(math.radians(d))-b*math.sin(math.radians(d))
    b1=a*math.sin(math.radians(d))+b*math.cos(math.radians(d))
    return a1,b1

a,b,d=map(int,input().split())
a1,b1=rotate(a,b,d)
print(a1,b1)
