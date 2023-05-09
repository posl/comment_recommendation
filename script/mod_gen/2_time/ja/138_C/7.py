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

if __name__ == '__main__':
    main()