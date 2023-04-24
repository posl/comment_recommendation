Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d.values():
        ans += i * (n - i)
    print(ans // 2)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += N - i - 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i] == A[i+1]:
            ans += 1
    print(N*(N-1)//2 - ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        if a[i] != a[i-1]:
            ans += i
    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                ans += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                ans += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    count = 0
    for i in range(N):
        if A[i] != A[i+1]:
            count += 1
    print(count*(count-1)//2)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += N - (i + 1) - (A[i] - A[i - 1]) * (N - (i + 1))
    print(ans)

=======
Suggestion 9

def input():
    return sys.stdin.readline()

import sys
import math
from collections import defaultdict, deque
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from copy import deepcopy
from operator import itemgetter

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aをソート
    A.sort()
    #Aの最大値がA[0]に来るようにする
    A.reverse()
    #Aの要素の個数を数える
    count = [0] * (A[0]+1)
    for i in range(N):
        count[A[i]] += 1
    #countを累積和
    for i in range(1,A[0]+1):
        count[i] += count[i-1]
    #出力
    print(sum(count))
