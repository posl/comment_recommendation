Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate(x,y,d):
    x1 = x*math.cos(math.radians(d)) - y*math.sin(math.radians(d))
    y1 = x*math.sin(math.radians(d)) + y*math.cos(math.radians(d))
    return x1,y1

=======
Suggestion 2

def rotate(x, y, d):
    import math
    rad = math.radians(d)
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

x, y, d = map(int, input().split())
x, y = rotate(x, y, d)
print(x, y)

=======
Suggestion 3

def rotate(a, b, d):
    import math
    rad = d * math.pi / 180
    a_ = a * math.cos(rad) - b * math.sin(rad)
    b_ = a * math.sin(rad) + b * math.cos(rad)
    return a_, b_

a, b, d = map(int, input().split())
a_, b_ = rotate(a, b, d)
print(a_, b_)

=======
Suggestion 4

def rotate(x, y, d):
    import math
    r = math.radians(d)
    x1 = x*math.cos(r) - y*math.sin(r)
    y1 = x*math.sin(r) + y*math.cos(r)
    return x1, y1

a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

=======
Suggestion 5

def rotate_point(a, b, d):
    import math
    rad = math.radians(d)
    a_new = a*math.cos(rad) - b*math.sin(rad)
    b_new = a*math.sin(rad) + b*math.cos(rad)
    return a_new, b_new

=======
Suggestion 6

def rotate(x,y,d):
    import math
    theta = math.radians(d)
    x1 = x*math.cos(theta)-y*math.sin(theta)
    y1 = x*math.sin(theta)+y*math.cos(theta)
    return x1,y1

x,y,d = map(int,input().split())
x1,y1 = rotate(x,y,d)
print(x1,y1)

=======
Suggestion 7

def main():
    import math
    a,b,d = input().split()
    a = float(a)
    b = float(b)
    d = float(d)
    rad = math.radians(d)
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    print(x,y)

=======
Suggestion 8

def rotate(a,b,d):
    from math import sin, cos, radians
    rad = radians(d)
    a1 = a*cos(rad) - b*sin(rad)
    b1 = a*sin(rad) + b*cos(rad)
    return a1,b1

=======
Suggestion 9

def main():
    a, b, d = map(int, input().split())
    # d = d % 360
    # print(d)
    # print(a, b, d)
    from math import cos, sin, radians
    # print(cos(radians(d)), sin(radians(d)))
    # print(cos(radians(d)) * a - sin(radians(d)) * b, sin(radians(d)) * a + cos(radians(d)) * b)
    print(cos(radians(d)) * a - sin(radians(d)) * b, sin(radians(d)) * a + cos(radians(d)) * b)

=======
Suggestion 10

def rotate_point(a,b,d):
    # a,b are the coordinates of the point
    # d is the degree of rotation
    import math
    d = math.radians(d)
    a_new = a*math.cos(d) - b*math.sin(d)
    b_new = a*math.sin(d) + b*math.cos(d)
    return a_new, b_new

a,b,d = map(float, input().split())
a_new, b_new = rotate_point(a,b,d)
print(a_new, b_new)
