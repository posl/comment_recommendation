Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate_point(x,y,d):
    import math
    rad = math.radians(d)
    new_x = x*math.cos(rad) - y*math.sin(rad)
    new_y = x*math.sin(rad) + y*math.cos(rad)
    return new_x,new_y

=======
Suggestion 2

def rotate(x, y, d):
    import math
    x1 = x * math.cos(math.radians(d)) - y * math.sin(math.radians(d))
    y1 = x * math.sin(math.radians(d)) + y * math.cos(math.radians(d))
    return (x1, y1)

=======
Suggestion 3

def rotate(x, y, d):
    import math
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    return x * cos - y * sin, x * sin + y * cos

=======
Suggestion 4

def rotate(a, b, d):
    import math
    rad = (d/180.0)*math.pi
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    return (x,y)

=======
Suggestion 5

def rotate(x,y,d):
    import math
    rad=math.radians(d)
    x1=x*math.cos(rad)-y*math.sin(rad)
    y1=x*math.sin(rad)+y*math.cos(rad)
    return x1,y1

=======
Suggestion 6

def rotate(x, y, d):
    import math
    d = math.radians(d)
    x1 = x * math.cos(d) - y * math.sin(d)
    y1 = x * math.sin(d) + y * math.cos(d)
    return x1, y1

x, y, d = map(int, input().split())
x1, y1 = rotate(x, y, d)
print(x1, y1)

=======
Suggestion 7

def rotate(a,b,d):
    import math
    d = math.radians(d)
    a_ = a * math.cos(d) - b * math.sin(d)
    b_ = a * math.sin(d) + b * math.cos(d)
    return a_,b_

a,b,d = map(float,input().split())
a_,b_ = rotate(a,b,d)
print(a_,b_)

=======
Suggestion 8

def rotate(a,b,d):
    import math
    x = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
    y = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))
    return x,y

a,b,d = map(int,input().split())
print(rotate(a,b,d))

=======
Suggestion 9

def rotate(a, b, d):
    import math
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    return x, y

=======
Suggestion 10

def rotate(x,y,d):
    import math
    d = math.radians(d)
    x_ = x*math.cos(d) - y*math.sin(d)
    y_ = x*math.sin(d) + y*math.cos(d)
    return x_,y_
