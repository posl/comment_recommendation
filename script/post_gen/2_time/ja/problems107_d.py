Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i] + b[i + 1]
    ans = 0
    for i in range(n):
        ans += c[n] - c[i] - (b[i + 1] * (n - i))
    print(ans // n)

=======
Suggestion 2

def median_of_three(a, b, c):
    if a < b:
        if b < c:
            return b
        elif c < a:
            return a
        else:
            return c
    else:
        if a < c:
            return a
        elif c < b:
            return b
        else:
            return c

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = N * (N + 1) // 2
    B = [0] * M
    b = 0
    for i in range(N):
        for j in range(i, N):
            B[b] = A[j]
            b += 1
    B.sort()
    print(B[M // 2])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = N * (N + 1) // 2
    ans = 0
    for i in range(N):
        ans += (N - i) * (i + 1) * A[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和を求める
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + A[i])
    # 累積和の差の絶対値を求める
    diff = [0]
    for i in range(N):
        diff.append(abs(cumsum[i+1] - cumsum[i]))
    # 累積和の差の絶対値の中央値を求める
    diff.sort()
    print(diff[N//2])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = []
    for i in range(N):
        C.append(B.index(A[i]))
    D = []
    for i in range(N):
        D.append(C[i] - i)
    E = sorted(D)
    F = []
    for i in range(N):
        F.append(E.index(D[i]))
    G = []
    for i in range(N):
        G.append(B[F[i]])
    print(G[N//2])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 2つの要素の中央値を求める
    def median(a, b):
        return (a + b) // 2

    # 3つの要素の中央値を求める
    def median3(a, b, c):
        if a > b:
            if c > a:
                return a
            elif c > b:
                return c
            else:
                return b
        else:
            if c > b:
                return b
            elif c > a:
                return c
            else:
                return a

    # 単純な中央値を求める
    def simple_median(a, b, c):
        if a > b:
            if c > a:
                return a
            elif c > b:
                return c
            else:
                return b
        else:
            if c > b:
                return b
            elif c > a:
                return c
            else:
                return a

    # 3つの要素の中央値を求める(別解)
    def median3_2(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return b

    # 3つの要素の中央値を求める(別解)
    def median3_3(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        return b

    # 3つの要素の中央値を求める(別解)
    def median3_4(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return b

    # 3つの要素の中央値を求める(別解)
    def

=======
Suggestion 8

def input():
    return sys.stdin.readline()[:-1]

import sys
import math
from collections import defaultdict
from collections import deque
from collections import Counter
from heapq import heappush, heappop

=======
Suggestion 9

def main():
    N = int(input())

    A = list(map(int, input().split()))

    # 中央値を求める関数
    def median(A):
        n = len(A)
        A.sort()
        if n % 2 == 0:
            return (A[n // 2 - 1] + A[n // 2]) / 2
        else:
            return A[n // 2]

    # mの中央値を求める
    M = []
    for i in range(N):
        for j in range(i, N):
            M.append(median(A[i:j + 1]))

    print(median(M))
