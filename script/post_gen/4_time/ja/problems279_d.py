Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    A, B = map(int, input().split())
    if B == 1:
        print(A)
        return
    if A == 1:
        print(1)
        return
    if A == 2:
        print(2)
        return
    # (A/((g)^(1/2))) = B*t + A
    # (g)^(1/2) = A/(B*t+A)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    # g = A^2/(B^2*t^2 + 2*A*B*t + A^2)
    t = 1
    while True:
        g = A**2/(B**2*t**2 + 2*A*B*t + A**2)
        if g < 1:
            print(t + A/(g**0.5))
            return
        t += 1

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print((A + B) ** 0.5)

=======
Suggestion 3

def main():
    from math import sqrt
    a, b = map(int, input().split())
    print((a / sqrt(b)) * 2)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print((A**0.5)*B)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print((A / ((B) ** (1/2))))

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print((A*B)**(1/2))

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    print((a+b**2)**0.5)

=======
Suggestion 8

def solve():
    import sys
    import math

    # 標準入力
    a, b = map(int, input().split())

    # 処理
    # 1回以上操作する場合
    if a >= b:
        # 1回目の操作を行うまでにかかる時間
        time = 1
        # 2回目以降の操作を行うまでにかかる時間
        time += b
        # 2回目以降の操作を行った後にかかる時間
        time += a / math.sqrt(b)
        # 結果出力
        print(time)
    # 1回も操作しない場合
    else:
        # 結果出力
        print(a)

=======
Suggestion 9

def solve():
    a,b = map(int,input().split())
    if a >= b:
        print(a)
        return
    else:
        print(a + b/2)

=======
Suggestion 10

def main():
    A, B = map(int, input().split())
    print(1 + (A-1) * B / 2)
