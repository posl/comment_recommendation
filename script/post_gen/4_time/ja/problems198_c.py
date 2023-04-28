Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    r, x, y = map(int, input().split())
    if r * r == x * x + y * y:
        print(1)
    elif r * r > x * x + y * y:
        print(2)
    else:
        print((x * x + y * y + r * r - 1) // (r * r))

=======
Suggestion 2

def solve():
    R, X, Y = map(int, input().split())

    if R**2 == X**2 + Y**2:
        print(1)
    elif R**2 > X**2 + Y**2:
        print(2)
    else:
        ans = 0
        while R**2 < X**2 + Y**2:
            ans += 1
            X = X // 2
            Y = Y // 2
        print(ans)

=======
Suggestion 3

def solve():
    r, x, y = map(int, input().split())
    d = (x ** 2 + y ** 2) ** 0.5
    if d % r == 0:
        print(int(d / r))
    elif d < r:
        print(2)
    else:
        print(int(d // r) + 1)

=======
Suggestion 4

def main():
    r, x, y = map(int, input().split())
    distance = (x**2 + y**2)**(1/2)
    if distance == r:
        print(1)
    elif distance <= 2*r:
        print(2)
    else:
        print(int(distance//r) + (distance%r != 0))

=======
Suggestion 5

def solve():
    R, X, Y = map(int, input().split())
    D = (X**2 + Y**2)**0.5
    if D < R:
        print(2)
    else:
        print(int(D//R + (D%R != 0)))
solve()

=======
Suggestion 6

def main():
    R,X,Y = map(int,input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5//R + 1))

=======
Suggestion 7

def solve():
    R, X, Y = map(int, input().split())

    dist = (X**2 + Y**2)**0.5

    if dist < R:
        print(2)
    else:
        print(int(dist//R + (dist%R != 0)))

=======
Suggestion 8

def solve():
    import sys
    R,X,Y = map(int, sys.stdin.readline().split())
    import math
    d = math.sqrt(X**2+Y**2)
    if d < R:
        print(2)
    else:
        print(math.ceil(d/R))

=======
Suggestion 9

def solve():
    # R X Y が与えられる
    R, X, Y = map(int, input().split())
    # 2点間の距離を求める
    distance = (X**2 + Y**2)**(1/2)
    # 距離がRより小さい場合
    if distance < R:
        # 原点から1歩進んだ時点で到達できる
        print(2)
    else:
        # 原点から1歩進んだ時点で到達できない
        # 原点からRずつ進んだ時点で到達できる
        print(int(distance // R) + 1)

=======
Suggestion 10

def cnt_step(r, x, y):
    if r**2 == x**2 + y**2:
        return int(r)
    elif r**2 > x**2 + y**2:
        return int(r+1)
    else:
        cnt = 0
        while True:
            if r**2 == x**2 + y**2:
                return int(cnt)
            elif r**2 > x**2 + y**2:
                return int(cnt+2)
            else:
                cnt += 2
                r += 1

r, x, y = map(int, input().split())

print(cnt_step(r, x, y))
