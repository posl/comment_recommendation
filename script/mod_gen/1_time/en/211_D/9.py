def main():
    import sys
    from collections import deque
    import math
    from functools import reduce
    import operator
    from itertools import accumulate
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from copy import deepcopy
    from itertools import combinations, permutations, product, combinations_with_replacement
    from collections import deque, Counter, defaultdict
    from operator import itemgetter, attrgetter
    from math import gcd, factorial
    def I(): return int(sys.stdin.readline())
    def LI(): return list(map(int, sys.stdin.readline().split()))
    def LS(): return sys.stdin.readline().split()
    def LLI(rows_number): return [LI() for _ in range(rows_number)]
    def LLS(rows_number): return [LS() for _ in range(rows_number)]
    def SI(): return sys.stdin.readline().strip()
    def DI(): return dict(Counter(LI()))
    def LDI(): return [DI() for _ in range(N)]
    def LI_(): return [int(i) - 1 for i in sys.stdin.readline().split()]
    def LF(): return [float(i) for i in sys.stdin.readline().split()]
    def LFI(rows_number): return [LF() for _ in range(rows_number)]
    def LFI_(rows_number): return [[int(i) - 1 for i in sys.stdin.readline().split()] for _ in range(rows_number)]
    sys.setrecursionlimit(200000)
    INF = 10 ** 18
    MOD = 10 ** 9 + 7
    #MOD = 998244353
    eps = 10 ** -10
    def modinv(n, p):
        return pow(n, p - 2, p)
    def comb(n, r, p):
        if n < r:
            return 0
        if n == r:
            return 1
        if r == 0:
            return 1
        if r == 1:
            return n
        if r == 2:
            return n * (n - 1) // 2
        if r == 3:
            return n * (n - 1) * (n - 2) // 6
        return comb(n - 1, r, p) + comb(n - 1, r

if __name__ == '__main__':
    main()