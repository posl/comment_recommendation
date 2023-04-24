Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N - 1):
        v[i + 1] = (v[i] + v[i + 1]) / 2
    print(v[-1])

=======
Suggestion 4

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[N-1])

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[0] = (v[0] + v[1]) / 2
        v.sort()
    print(v[0])

=======
Suggestion 6

def main():
    N = int(input())
    v = list(map(int,input().split()))
    v.sort()
    while len(v) > 1:
        x = v.pop(0)
        y = v.pop(0)
        v.append((x+y)/2)
        v.sort()
    print(v[0])

=======
Suggestion 7

def solve():
    N = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    while len(v) > 1:
        x = v.pop(0)
        y = v.pop(0)
        v.append((x + y) / 2)
        v.sort()
    print(v[0])

=======
Suggestion 8

def main():
    import sys
    from io import StringIO
    import unittest
    import math
    import itertools
    from collections import Counter
    from collections import defaultdict
    from collections import deque
    from heapq import heappush, heappop
    from bisect import bisect_left, bisect_right
    import copy

    def I(): return int(sys.stdin.readline())
    def LI(): return list(map(int, sys.stdin.readline().split()))
    def LS(): return sys.stdin.readline().split()
    def S(): return sys.stdin.readline().strip()
    def IR(n): return [I() for i in range(n)]
    def LIR(n): return [LI() for i in range(n)]
    def LRS(n): return [LS() for i in range(n)]
    def SR(n): return [S() for i in range(n)]
    def LSR(n): return [list(S()) for i in range(n)]
    def SRL(n): return [[i for i in S()] for i in range(n)]
    def MSRL(n): return [[int(i) for i in S()] for i in range(n)]
    sys.setrecursionlimit(1000000)
    mod = 1000000007

    n = I()
    v = LI()
    ans = 0
    for i in range(1, n):
        v.sort()
        ans = (v[0] + v[1]) / 2
        v[0] = ans
        v[1] = 1000
    print(ans)
