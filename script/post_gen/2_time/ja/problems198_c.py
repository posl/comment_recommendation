Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) < R**2:
        print(2)
    else:
        print((X**2 + Y**2)**(1/2) // R + 1)

=======
Suggestion 2

def solve():
    R, X, Y = map(int, input().split())
    if R*R == X*X + Y*Y:
        print(1)
        return
    if R*R > X*X + Y*Y:
        print(2)
        return
    if R*R < X*X + Y*Y:
        import math
        print(math.ceil((X*X + Y*Y)**(1/2) / R))
        return

=======
Suggestion 3

def solve():
    R, X, Y = map(int, input().split())
    d = (X**2 + Y**2)**0.5
    if d < R:
        print(2)
    else:
        print(int(d/R)+1)

=======
Suggestion 4

def solve():
    R, X, Y = map(int, input().split())
    if X**2 + Y**2 == R**2:
        return 1
    if X**2 + Y**2 <= R**2*4:
        return 2
    return -(-int((X**2 + Y**2)**(1/2))//R)
print(solve())

=======
Suggestion 5

def solve():
    import sys
    R, X, Y = map(int, sys.stdin.readline().split())
    d = (X**2 + Y**2)**0.5
    if d < R:
        print(2)
    else:
        print(int(d//R + 1))

=======
Suggestion 6

def solve():
    R,X,Y = map(int,input().split())
    if (X**2+Y**2)**0.5 == R:
        print(1)
        return
    if (X**2+Y**2)**0.5 <= 2*R:
        print(2)
        return
    print(int((X**2+Y**2)**0.5//R)+1)

=======
Suggestion 7

def solve():
    import sys
    readline = sys.stdin.readline

    r, x, y = map(int, readline().split())
    if x**2 + y**2 < r**2:
        print(2)
    else:
        print((x**2 + y**2 + r**2 - 1)//(r**2))

=======
Suggestion 8

def main():
    R,X,Y = map(int,input().split())
    distance = (X**2 + Y**2)**(1/2)
    if distance.is_integer():
        print(int(distance//R))
    else:
        print(int(distance//R + 1))

=======
Suggestion 9

def solve():
    import sys
    input = sys.stdin.readline
    from math import ceil
    r, x, y = map(int, input().split())
    dist = (x**2 + y**2) ** 0.5
    if dist < r:
        print(2)
    else:
        print(ceil(dist/r))

=======
Suggestion 10

def main():
    import sys
    import math

    # 標準入力
    r, x, y = map(int, sys.stdin.readline().split())

    # 処理
    # 1歩で移動できる距離
    r1 = math.sqrt(x**2 + y**2)
    if r1 == r:
        print(1)
    elif r1 <= r*2:
        print(2)
    else:
        print(math.ceil(r1/r))
