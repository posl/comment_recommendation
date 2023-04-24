Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    R, X, Y = map(int, input().split())
    if R * R == X * X + Y * Y:
        print(1)
    elif R * R > X * X + Y * Y:
        print(2)
    else:
        ans = 0
        while True:
            ans += 1
            if (R * ans) * (R * ans) >= X * X + Y * Y:
                break
        print(ans)

=======
Suggestion 2

def solve():
    R, X, Y = map(int, input().split())
    if R*R == X*X + Y*Y:
        print(1)
    elif R*R > X*X + Y*Y:
        print(2)
    else:
        print((X*X + Y*Y + R*R - 1)//(R*R))

=======
Suggestion 3

def solve():
    R, X, Y = map(int, input().split())
    if R*R > X*X + Y*Y:
        print(2)
    else:
        print(int((X*X + Y*Y)**0.5/R)+1)

=======
Suggestion 4

def solve():
    import sys
    R,X,Y = map(int,sys.stdin.readline().split())
    if R*R > X*X + Y*Y:
        print(2)
    else:
        print((X*X + Y*Y + R*R - 1)//(R*R))

=======
Suggestion 5

def solve():
    r,x,y = list(map(int,input().split()))
    if r**2 == x**2 + y**2:
        print(1)
        return
    if r**2 > x**2 + y**2:
        print(2)
        return
    print(math.ceil((x**2 + y**2)**(1/2)/r))

=======
Suggestion 6

def solve():
    import sys
    input = sys.stdin.readline
    from math import ceil

    R, X, Y = map(int, input().split())

    if R**2 == X**2 + Y**2:
        print(1)
    elif R**2 > X**2 + Y**2:
        print(2)
    else:
        print(ceil((X**2 + Y**2)**0.5 / R))

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    import math

    R, X, Y = map(int, input().split())

    if X**2 + Y**2 == R**2:
        print(1)
    elif X**2 + Y**2 < R**2:
        print(2)
    else:
        print(math.ceil(math.sqrt(X**2 + Y**2)/R))

main()

=======
Suggestion 8

def resolve():
    import sys
    import math
    input = sys.stdin.readline
    r,x,y = map(int,input().split())
    if r**2 > x**2 + y**2:
        print(2)
    else:
        print(math.ceil((x**2 + y**2) ** 0.5 / r))

=======
Suggestion 9

def solve():
    # R, X, Y = map(int, input().split())
    # # R, X, Y = 5, 11, 0
    # # R, X, Y = 5, 15, 0
    # # R, X, Y = 3, 4, 4
    # if R*R > X*X + Y*Y:
    #     print(2)
    # else:
    #     print(1 + (X*X + Y*Y) // (R*R))
    R, X, Y = map(int, input().split())
    d = X*X + Y*Y
    if d < R*R:
        print(2)
    elif d == R*R:
        print(1)
    else:
        print((d + R*R - 1) // (R*R))

=======
Suggestion 10

def main():
    import sys
    from math import sqrt

    readline = sys.stdin.buffer.readline
    #read = sys.stdin.buffer.read
    #readlines = sys.stdin.buffer.readlines

    r,x,y = map(int,readline().split())
    d = sqrt(x**2+y**2)
    if d < r:
        print(2)
    else:
        print(int(d//r)+1)
