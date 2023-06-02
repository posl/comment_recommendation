Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate(a, b, d):
    import math
    rad = math.radians(d)
    return a * math.cos(rad) - b * math.sin(rad), a * math.sin(rad) + b * math.cos(rad)

=======
Suggestion 2

def rotate(x, y, d):
    d = d/180*3.1415926535897932384626
    x1 = x * math.cos(d) - y * math.sin(d)
    y1 = x * math.sin(d) + y * math.cos(d)
    return x1, y1

=======
Suggestion 3

def rotate(x,y,d):
    import math
    d = math.radians(d)
    a = x*math.cos(d) - y*math.sin(d)
    b = x*math.sin(d) + y*math.cos(d)
    return a,b

=======
Suggestion 4

def rotate(a,b,d):
    import math
    d = math.radians(d)
    x = a*math.cos(d) - b*math.sin(d)
    y = a*math.sin(d) + b*math.cos(d)
    return x,y

a,b,d = map(int,input().split())
x,y = rotate(a,b,d)
print(x,y)

=======
Suggestion 5

def get_new_point(a,b,d):
    import math
    a = float(a)
    b = float(b)
    d = float(d)
    d = math.radians(d)
    x = a*math.cos(d)-b*math.sin(d)
    y = a*math.sin(d)+b*math.cos(d)
    return x,y

=======
Suggestion 6

def problems259_b():
    pass

=======
Suggestion 7

def rotate(a, b, d):
    from math import sin, cos, radians
    d = radians(d)
    x = a * cos(d) - b * sin(d)
    y = a * sin(d) + b * cos(d)
    return x, y

=======
Suggestion 8

def rotate(x,y,degree):
    degree = degree/180*3.14159265358979323846264338327950288
    x1 = x * math.cos(degree) - y * math.sin(degree)
    y1 = x * math.sin(degree) + y * math.cos(degree)
    return x1,y1

=======
Suggestion 9

def rotate(a, b, d):
    import math
    x = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
    y = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
    return x, y

=======
Suggestion 10

def problem259_b():
    a, b, d = map(int, input().split())
    x = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
    y = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
    print(x, y)

problem259_b()
