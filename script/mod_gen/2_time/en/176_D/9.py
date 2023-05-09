def main():
    import sys
    import math
    from collections import deque
    from collections import defaultdict
    from collections import Counter
    from itertools import combinations
    from itertools import permutations
    from itertools import product
    from bisect import bisect_left
    from bisect import bisect_right
    from functools import lru_cache
    from heapq import heappush, heappop
    from math import factorial
    from math import gcd
    from math import log2
    from math import inf
    from operator import itemgetter
    from operator import mul
    from operator import xor
    from string import ascii_lowercase
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    def read_int(): return int(input())
    def read_int_n(): return list(map(int, input().split()))
    def read_float(): return float(input())
    def read_float_n(): return list(map(float, input().split()))
    def read_str(): return input().rstrip()
    def read_str_n(): return list(map(str, input().split()))
    def error_print(*args): print(*args, file=sys.stderr)
    INF = 10**18
    MOD = 10**9+7
    # MOD = 998244353
    H, W = read_int_n()
    Ch, Cw = read_int_n()
    Dh, Dw = read_int_n()
    S = [read_str() for _ in range(H)]
    dist = [[INF]*W for _ in range(H)]
    dist[Ch-1][Cw-1] = 0
    que = deque([(Ch-1, Cw-1)])
    while que:
        h, w = que.popleft()
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h+dh, w+dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == '#':
                continue
            if dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            que.appendleft((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2,

if __name__ == '__main__':
    main()