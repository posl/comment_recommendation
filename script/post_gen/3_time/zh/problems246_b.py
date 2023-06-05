Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B = map(int, input().split())
    print(A/B)
    print(A//B)
    print(A%B)

=======
Suggestion 2

def problem246_b():
    A,B = map(int, input().split())
    x = A/(A**2+B**2)**0.5
    y = B/(A**2+B**2)**0.5
    print('{:.12f} {:.12f}'.format(x,y))

=======
Suggestion 3

def distance(x, y):
    return (x**2 + y**2)**0.5

=======
Suggestion 4

def problems246_b():
    import math
    A, B = map(int, input().split())
    x = (A**2 + B**2) ** 0.5
    y = math.atan(B/A)
    print(x*math.cos(y), x*math.sin(y))

problems246_b()

=======
Suggestion 5

def getDistance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 6

def problems246_b():
    a, b = map(int, input().split())
    x = a / (a ** 2 + b ** 2) ** 0.5
    y = b / (a ** 2 + b ** 2) ** 0.5
    print(x, y)

=======
Suggestion 7

def main():
    A,B = map(int, input().split())
    x = A/(A**2+B**2)**0.5
    y = B/(A**2+B**2)**0.5
    print(x,y)

=======
Suggestion 8

def f(x, y):
    c = (x**2 + y**2)**0.5
    return x/c, y/c

a, b = map(int, input().split())
x, y = f(a, b)
print(x, y)

=======
Suggestion 9

def problems246_b():
    a,b = map(int, input().split())
    print(a/b, b/a)

=======
Suggestion 10

def problems246_b():
    a, b = map(int, input().split())
    x = b / (a ** 2 + b ** 2) ** 0.5
    y = a / (a ** 2 + b ** 2) ** 0.5
    print(x, y)

problems246_b()
