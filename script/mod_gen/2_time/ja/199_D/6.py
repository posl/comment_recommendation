def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    from collections import deque
    from collections import defaultdict
    from itertools import accumulate
    from itertools import combinations
    from itertools import permutations
    from itertools import product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from copy import deepcopy
    from math import gcd
    from math import factorial
    from math import ceil
    from math import floor
    from math import sqrt
    from math import log2
    from math import log10
    from math import pi
    from math import sin
    from math import cos
    from math import tan
    from math import asin
    from math import acos
    from math import atan
    from math import sinh
    from math import cosh
    from math import tanh
    from math import asinh
    from math import acosh
    from math import atanh
    from operator import mul
    from operator import itemgetter
    from operator import attrgetter
    from functools import lru_cache
    from functools import reduce
    from functools import partial
    from string import ascii_lowercase
    from string import ascii_uppercase
    from string import digits
    #from numba import njit
    #@njit
    def solve():
        N, M = map(int, input().split())
        AB = [list(map(int, input().split())) for _ in range(M)]
        if M == 0:
            print(3**N)
            return
        AB = [sorted(i) for i in AB]
        AB.sort()
        AB = list(accumulate(AB))
        def check(x):
            for i in range(M):
                if AB[i][0] == x:
                    return False
            return True
        ans = 0
        for i in range(3**N):
            x = i
            cnt = 0
            flag = True
            for j in range(N):
                if not check(j+1):
                    continue
                if x % 3 == 1:
                    cnt += 1
                elif x % 3 == 2:
                    cnt += 2
                if cnt > 2:
                    flag = False
                    break

if __name__ == '__main__':
    main()