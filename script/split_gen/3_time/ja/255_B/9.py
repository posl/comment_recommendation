def solve():
    import sys
    readline = sys.stdin.readline
    from math import sqrt
    from collections import deque
    from bisect import bisect_left
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    A = [a-1 for a in A]
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, readline().split())
    def is_ok(R):
        # Rが与えられた時、K人の人がRの明かりを持っている時、
        # すべての人が少なくとも1つの明かりによって照らされるか判定する
        # すべて
