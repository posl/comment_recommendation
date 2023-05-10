Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((a + b - 1) / b)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(((A/B)**0.5)*B)

=======
Suggestion 3

def solve():
    a, b = map(int, input().split())
    print((a * b**2)**0.5 - b)

=======
Suggestion 4

def calc(a, b):
    return a + ((b)/((2)^(1/2)))

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    print((A+(B/2))/(B**0.5))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print((a + b) ** 0.5)

=======
Suggestion 8

def main():
    import sys
    import math
    readline = sys.stdin.readline

    a, b = map(int, readline().rstrip().split())
    g = 1
    t = 0
    while g <= b:
        g += 1
        t += a / math.sqrt(g)
    print(t)

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    ans = 0
    print(ans)

=======
Suggestion 10

def main():
    A, B = map(int, input().split())

    if A == 1:
        print(1)
        return

    # 二分探索
    # 1回目の操作でgを1増やすと、落下時間はA/((g+1)^(1/2))となる
    # 2回目の操作でgを1増やすと、落下時間はA/((g+2)^(1/2))となる
    # となるので、落下時間の増加は減少していく
    # 二分探索で、落下時間がBを超える最小の回数を求める
    # その回数-1が答え
    left = 0
    right = 10**18
    while left < right:
        mid = (left + right) // 2
        if A / ((mid + 1)**0.5) - A / ((mid + 2)**0.5) > B:
            left = mid + 1
        else:
            right = mid
    print(left - 1)
