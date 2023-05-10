def main():
    # import sys
    # import math
    # from collections import Counter
    # from collections import deque
    # from decimal import Decimal
    # from decimal import getcontext
    # from itertools import accumulate
    # from itertools import combinations
    # from itertools import combinations_with_replacement
    # from itertools import groupby
    # from itertools import permutations
    # from itertools import product
    # from operator import itemgetter
    # from operator import mul
    # from operator import xor
    # from operator import add
    # from operator import sub
    # from operator import truediv
    # from operator import floordiv
    # from functools import reduce
    # from functools import lru_cache
    # from functools import partial
    # from bisect import bisect_left
    # from bisect import bisect_right
    # sys.setrecursionlimit(1000000)
    # getcontext().prec = 28
    n = int(input())
    moves = [tuple(map(int, input().split())) for _ in range(n)]
    moves.sort()
    dp = [0] * (n + 1)
    for i in range(n):
        t, k, *a = moves[i]
        dp[i + 1] = t
        for j in range(k):
            dp[i + 1] = max(dp[i + 1], dp[a[j]] + t)
    print(dp[-1])
