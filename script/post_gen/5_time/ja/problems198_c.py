Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    R, X, Y = map(int, input().split())
    if R ** 2 == X ** 2 + Y ** 2:
        print(1)
    elif R ** 2 > X ** 2 + Y ** 2:
        print(2)
    else:
        print(math.ceil((X ** 2 + Y ** 2) ** 0.5 / R))

=======
Suggestion 2

def main():
    import sys
    import math
    r,x,y=map(int,input().split())
    d=math.sqrt(x*x+y*y)
    if d==r:
        print(1)
    elif d<=2*r:
        print(2)
    else:
        print(math.ceil(d/r))

=======
Suggestion 3

def solve():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) % R**2 == 0:
        print((X**2 + Y**2) // R**2)
    else:
        print((X**2 + Y**2) // R**2 + 1)

=======
Suggestion 4

def main():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) < R**2:
        print(2)
    else:
        print(int(((X**2 + Y**2)**0.5 + R - 1)//R))

=======
Suggestion 5

def solve():
    R, X, Y = map(int, input().split())
    if X*X + Y*Y < R*R:
        print(2)
    else:
        print((X*X+Y*Y)**(1/2)//R + (1 if (X*X+Y*Y)**(1/2)%R != 0 else 0))

=======
Suggestion 6

def main():
    r, x, y = map(int, input().split())
    d = (x**2 + y**2)**(1/2)
    if d < r:
        print(2)
    else:
        print(int(d//r) + int(d%r > 0))

=======
Suggestion 7

def solve():
    R, X, Y = map(int, input().split())
    d = (X**2 + Y**2)**0.5
    if d == R:
        print(1)
    elif d <= 2*R:
        print(2)
    else:
        print(int(d//R + (d%R != 0)))

=======
Suggestion 8

def solve():
    R, X, Y = map(int, input().split())
    d = (X*X+Y*Y)**(1/2)
    if d < R:
        print(2)
    else:
        print(int(d//R) + int(d%R != 0))

=======
Suggestion 9

def main():
    import sys
    import math
    R,X,Y = map(int, sys.stdin.readline().split())
    dist = math.sqrt(X**2 + Y**2)
    if dist < R:
        print(2)
    else:
        print(math.ceil(dist/R))

=======
Suggestion 10

def solve():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    R, X, Y = map(int, input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print((X**2 + Y**2)**0.5 // R + 1)
