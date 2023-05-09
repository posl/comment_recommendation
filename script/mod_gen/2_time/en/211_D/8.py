def main():
    import sys
    from collections import deque
    from collections import defaultdict
    from fractions import gcd
    from functools import reduce
    from math import sqrt, ceil, floor, factorial
    from heapq import heappush, heappop, heapify
    from itertools import combinations, permutations, accumulate, product
    from operator import mul
    from bisect import bisect_left, bisect_right
    from copy import deepcopy
    from decimal import *
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 20
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    pi = Decimal(3.1415926535897932384626433832795028841971)
    def inp(): return sys.stdin.readline().rstrip("\r
")  # for fast input
    def out(var): sys.stdout.write(str(var))  # for fast output, always take string
    def lis(): return list(map(int, inp().split()))
    def stringlis(): return list(map(str, inp().split()))
    def sep(): return map(int, inp().split())
    def strsep(): return map(str, inp().split())
    def fsep(): return map(float, inp().split())
    def nextline(): out("\n")  # as stdout.write always print sring.
    def testcase(t):
        for p in range(t):
            solve()
    def printlist(a):
        for p in range(0, len(a)):
            out(str(a[p]) + ' ')
    def lcm(a, b): return (a * b) // gcd(a, b)
    def power(x, y, p):
        res = 1
        x = x % p
        if (x == 0):
            return 0
        while (y > 0):
            if ((y & 1) == 1):
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res
    def ncr(n, r, p):
        num = den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den,

if __name__ == '__main__':
    main()