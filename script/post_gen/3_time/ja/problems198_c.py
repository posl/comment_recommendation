Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    R, X, Y = map(int, input().split())
    distance = ((X ** 2) + (Y ** 2)) ** (1 / 2)
    if distance % R == 0:
        print(int(distance / R))
    else:
        print(int(distance // R) + 1)

=======
Suggestion 2

def main():
    R, X, Y = map(int, input().split())
    D = ((X ** 2) + (Y ** 2)) ** (1 / 2)
    if D == R:
        print(1)
    elif D <= 2 * R:
        print(2)
    else:
        if D % R == 0:
            print(int(D / R))
        else:
            print(int(D / R) + 1)

=======
Suggestion 3

def main():
    R, X, Y = map(int, input().split())
    distance = ((X**2)+(Y**2))**(1/2)
    if distance % R == 0:
        print(int(distance // R))
    else:
        print(int(distance // R+1))

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    r, x, y = map(int,input().split())
    d = (x**2+y**2)**(1/2)
    if d == r:
        print(1)
    elif d < r:
        print(2)
    else:
        if d % r == 0:
            print(int(d/r))
        else:
            print(int(d/r)+1)

=======
Suggestion 5

def main():
    r, x, y = map(int, input().split())
    # 距離を求める
    d = ((x**2)+(y**2))**(1/2)
    # 距離をrで割った余りが0なら、距離をrで割った商が答え
    if d%r == 0:
        print(int(d/r))
    # 距離をrで割った余りが0でないなら、距離をrで割った商に1を足したものが答え
    else:
        print(int(d/r)+1)

=======
Suggestion 6

def main():
    import math
    R, X, Y = map(int, input().split())
    if math.sqrt(X**2 + Y**2) <= R:
        print(2)
        return
    print(math.ceil(math.sqrt(X**2 + Y**2) / R))

=======
Suggestion 7

def main():
    #入力
    R, X, Y = map(int, input().split())
    #出力
    print(solve(R, X, Y))

=======
Suggestion 8

def main():
    import math
    R, X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        print(0)
        return
    if X == Y:
        print(int(math.sqrt(X**2 + Y**2) / R) + 1)
        return
    if X == 0:
        print(int(Y / R) + 1)
        return
    if Y == 0:
        print(int(X / R) + 1)
        return
    print(int(math.sqrt(X**2 + Y**2) / R) + 1)

=======
Suggestion 9

def main():
    R, X, Y = map(int, input().split())
    X = abs(X)
    Y = abs(Y)
    if X <= R and Y <= R:
        print(2)
    else:
        count = 0
        while True:
            if X <= R and Y <= R:
                break
            else:
                X -= R
                Y -= R
                count += 1
        print(count)

=======
Suggestion 10

def main():
    #入力
    R, X, Y = map(int, input().split())
    #出力
    print(1 + ((X**2 + Y**2)**(1/2) // R) + (1 if (X**2 + Y**2)**(1/2) % R != 0 else 0))
