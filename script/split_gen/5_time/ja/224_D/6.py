def solve():
    import sys
    input = sys.stdin.readline
    from collections import deque
    from heapq import heappush, heappop
    from bisect import bisect_left, bisect_right
    from math import ceil, floor, sqrt
    from itertools import permutations, combinations, product, accumulate
    from operator import itemgetter
    #sys.setrecursionlimit(10 ** 6)
    #INF = float("inf")
    INF = 10 ** 18
    MOD = 10 ** 9 + 7
    #MOD = 998244353
    #alp = "abcdefghijklmnopqrstuvwxyz"
    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.par = [-1] * n
            self.siz = [1] * n
        def root(self, x):
            if self.par[x] == -1:
                return x
            else:
                self.par[x] = self.root(self.par[x])
                return self.par[x]
        def issame(self, x, y):
            return self.root(x) == self.root(y)
        def unite(self, x, y):
            x = self.root(x)
            y = self.root(y)
            if x == y:
                return False
            if self.siz[x] < self.siz[y]:
                x, y = y, x
            self.par[y] = x
            self.siz[x] += self.siz[y]
            return True
        def size(self, x):
            return self.siz[self.root(x)]
    M = int(input())
    uf = UnionFind(9)
    for _ in range(M):
        u, v = map(int, input().split())
        uf.unite(u-1, v-1)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, 9):
        if not uf.issame(p[i-1]-1, p[i]-1):
            print(-1)
            exit()
    for i in range(1, 9):
        if not uf.issame(i-1, i):
            ans += 1
    print(ans)
