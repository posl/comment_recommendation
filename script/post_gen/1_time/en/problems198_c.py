Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    R, X, Y = map(int, input().split())
    if R*R == X*X + Y*Y:
        print(1)
    elif R*R > X*X + Y*Y:
        print(2)
    else:
        print((X*X + Y*Y + R*R - 1)//(R*R))

=======
Suggestion 2

def main():
    r, x, y = map(int, input().split())
    d = (x**2 + y**2)**(1/2)
    if d < r:
        print(2)
    else:
        print(int(d//r) + (d%r != 0))

=======
Suggestion 3

def solve():
    R, X, Y = map(int, input().split())
    if R*R == X*X + Y*Y:
        print(1)
    elif R*R > X*X + Y*Y:
        print(2)
    else:
        print(int((X*X + Y*Y)**0.5//R) + 1)
    return 0

=======
Suggestion 4

def main():
    import math
    R, X, Y = map(int, input().split())
    distance = math.sqrt(X**2 + Y**2)
    if distance == R:
        print(1)
    elif distance <= 2*R:
        print(2)
    else:
        print(math.ceil(distance/R))

=======
Suggestion 5

def solve():
    import math
    R, X, Y = map(int, input().split())
    d = math.sqrt(X*X + Y*Y)
    if d == R:
        print(1)
    elif d <= 2*R:
        print(2)
    else:
        print(math.ceil(d/R))

=======
Suggestion 6

def solve():
    R, X, Y = map(int, input().split())
    if (X*X+Y*Y)%(R*R)!=0:
        print((X*X+Y*Y)//(R*R)+1)
    else:
        print((X*X+Y*Y)//(R*R))
solve()

=======
Suggestion 7

def main():
    import sys
    import math
    r, x, y = map(int, sys.stdin.readline().split())
    d = math.sqrt(x * x + y * y)
    if d < r:
        print(2)
    else:
        print(math.ceil(d / r))

=======
Suggestion 8

def main():
    import math
    R,X,Y = map(int,input().split())
    distance = math.sqrt(X**2+Y**2)
    if distance%R == 0:
        print(int(distance/R))
    elif distance < R:
        print(2)
    else:
        print(int(distance//R+1))

=======
Suggestion 9

def solve():
    #import sys
    #input = sys.stdin.readline
    r,x,y = map(int,input().split())
    if r**2 > x**2 + y**2:
        print(2)
    else:
        print((x**2 + y**2)**(1/2)//r + 1)

=======
Suggestion 10

def main():
    # input
    r, x, y = map(int, input().split())
    # compute
    if (x ** 2 + y ** 2) // (r ** 2) == 0:
        ans = 2
    else:
        ans = ((x ** 2 + y ** 2) // (r ** 2)) ** (1 / 2)
    # output
    print(ans)
