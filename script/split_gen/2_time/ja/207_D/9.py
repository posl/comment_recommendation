def main():
    import sys
    import math
    import itertools
    import collections
    import bisect
    import heapq
    import copy
    import decimal
    import fractions
    import functools
    import operator
    import random
    sys.setrecursionlimit(1000000)
    INF = 10**20
    EPS = 10**-10
    MOD = 10**9 + 7
    PI = math.acos(-1)
    def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
    def I(): return int(sys.stdin.buffer.readline())
    def LS(): return sys.stdin.buffer.readline().rstrip().split()
    def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
    def IR(n): return [I() for _ in range(n)]
    def LIR(n): return [LI() for _ in range(n)]
    def SR(n): return [S() for _ in range(n)]
    def LSR(n): return [LS() for _ in range(n)]
    def SRL(n): return [list(S()) for _ in range(n)]
    def MSRL(n): return [[int(j) for j in list(S())] for _ in range(n)]
    random.seed(0)
    def solve():
        n = I()
        s = LIR(n)
        t = LIR(n)
        for i in range(360):
            p = i * PI / 180
            ss = [(s[i][0] * math.cos(p) - s[i][1] * math.sin(p), s[i][0] * math.sin(p) + s[i][1] * math.cos(p)) for i in range(n)]
            ss.sort()
            t.sort()
            if ss == t:
                print("Yes")
                return
        print("No")
    solve()
