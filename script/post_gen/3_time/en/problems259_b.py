Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,d = map(int,input().split())
    d = d * math.pi / 180
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    print(x,y)

=======
Suggestion 2

def rotate(a,b,d):
    import math
    d = math.radians(d)
    x = a * math.cos(d) - b * math.sin(d)
    y = a * math.sin(d) + b * math.cos(d)
    return x, y

a, b, d = input().split()
a = int(a)
b = int(b)
d = int(d)

x, y = rotate(a,b,d)

print(x, y)

=======
Suggestion 3

def main():
    a,b,d = map(int, input().split())
    d = d * math.pi / 180
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))

=======
Suggestion 4

def main():
    a, b, d = map(int, input().split())
    print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))

=======
Suggestion 5

def rotate(x, y, degree):
    import math
    r = math.radians(degree)
    x1 = x * math.cos(r) - y * math.sin(r)
    y1 = x * math.sin(r) + y * math.cos(r)
    return x1, y1

=======
Suggestion 6

def main():
    a, b, d = [int(i) for i in input().split()]
    d = d * math.pi / 180
    a = a * math.cos(d) - b * math.sin(d)
    b = a * math.sin(d) + b * math.cos(d)
    print(a, b)

=======
Suggestion 7

def main():
    a, b, d = map(int, input().split())
    d = d * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))

=======
Suggestion 8

def rotate(x,y,degree):
    import math
    degree = math.radians(degree)
    x = x * math.cos(degree) - y * math.sin(degree)
    y = x * math.sin(degree) + y * math.cos(degree)
    return x,y

=======
Suggestion 9

def main():
    from math import cos, sin, pi
    a, b, d = [int(i) for i in input().split()]
    d = d * pi / 180
    print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
