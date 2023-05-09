def main():
    from sys import stdin
    #from math import floor, sqrt, log, log2, log10, sin, cos, tan, pi, inf
    #from collections import deque
    #from itertools import permutations
    #from functools import lru_cache
    #from copy import deepcopy
    #from decimal import Decimal
    #from bisect import bisect_left, bisect_right
    #from heapq import heapify, heappush, heappop
    readline = stdin.readline
    #readlines = stdin.readlines
    #ns = lambda: readline().rstrip()
    #ni = lambda: int(readline().rstrip())
    #nm = lambda: map(int, readline().rstrip().split())
    #nl = lambda: list(map(int, readline().rstrip().split()))
    #nns = lambda: readline().rstrip().split()
    #nns_ = lambda: readline().rstrip().split('_')
    #nni = lambda: int(readline().rstrip().split())
    #nnm = lambda: map(int, readline().rstrip().split())
    #nnl = lambda: list(map(int, readline().rstrip().split()))
    #nnns = lambda: readline().rstrip().split()
    #nnns_ = lambda: readline().rstrip().split('_')
    #nnni = lambda: int(readline().rstrip().split())
    #nnnm = lambda: map(int, readline().rstrip().split())
    #nnnl = lambda: list(map(int, readline().rstrip().split()))
    n = int(input())
    a = list(map(int, input().split()))
    ans = 360
    for i in range(n):
        ans = min(ans, 360 - (a[i] + sum(a[i+1:])))
    print(ans)
