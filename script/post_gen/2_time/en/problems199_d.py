Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    print(solve(n, m, a, b))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    ans = 0
    for i in range(3**N):
        col = [i//(3**j)%3 for j in range(N)]
        if all(col[x] != col[y] for x, y in G):
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    edges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)

    colors = [0] * N
    count = 0
    def dfs(v):
        nonlocal count
        if v == N:
            count += 1
            return
        for c in range(3):
            colors[v] = c
            if all(colors[v] != colors[u] for u in edges[v]):
                dfs(v + 1)
    dfs(0)
    print(count)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3 ** N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [[a - 1, b - 1] for a, b in AB]
    AB = [sorted(a) for a in AB]
    AB.sort()
    AB = [[a, b] for a, b in AB if AB.count([a, b]) == 1]
    M = len(AB)
    if M == 0:
        print(0)
        return
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    c = [0] * N
    def dfs(v, p):
        if c[v] != 0:
            return
        c[v] = p
        for u in G[v]:
            dfs(u, 3 - p)
    dfs(0, 1)
    for v in range(N):
        if c[v] == 0:
            print(0)
            return
    for v in range(N):
        for u in G[v]:
            if c[v] == c[u]:
                print(0)
                return
    print(3 ** (N - M))

main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = 0
    for i in range(3**N):
        col = [0] * N
        for j in range(N):
            col[j] = (i // (3**j)) % 3
        ok = True
        for j in range(N):
            for k in G[j]:
                if col[j] == col[k]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
    else:
        print(0)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    print(solve(N, M, AB))

=======
Suggestion 8

def main():
    import sys
    import numpy as np
    N, M = map(int, sys.stdin.readline().split())
    if M == 0:
        print(3**N)
        return
    edges = np.zeros((N, N), dtype=np.int64)
    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        edges[A - 1][B - 1] = 1
        edges[B - 1][A - 1] = 1
    ans = 0
    for i in range(3**N):
        flag = True
        for j in range(N):
            for k in range(N):
                if edges[j][k] == 1 and (i // 3**j) % 3 == (i // 3**k) % 3:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**9
    dp = [[INF for _ in range(3)] for _ in range(N+1)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
    for i in range(M):
        if dp[AB[i][0]][0] == INF:
            print(0)
            return
        elif dp[AB[i][0]][1] == INF:
            print(0)
            return
        elif dp[AB[i][0]][2] == INF:
            print(0)
            return
        elif dp[AB[i][1]][0] == INF:
            print(0)
            return
        elif dp[AB[i][1]][1] == INF:
            print(0)
            return
        elif dp[AB[i][1]][2] == INF:
            print(0)
            return
        elif dp[AB[i][0]][0] == 1 and dp[AB[i][1]][0] == 1:
            print(0)
            return
        elif dp[AB[i][0]][0] == 1 and dp[AB[i][1]][1] == 1:
            print(0)
            return
        elif dp[AB[i][0]][0] == 1 and dp[AB[i][1]][2] == 1:
            print(0)
            return
        elif dp[AB[i][0]][1] == 1 and dp[AB[i][1]][0] == 1:
            print(0)
            return
        elif dp[AB[i][0]][1] == 1 and dp[AB[i][1]][

=======
Suggestion 10

def input():
    return sys.stdin.readline()[:-1]

import sys
import math
from collections import deque, Counter
from itertools import permutations, combinations
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import gcd
from functools import reduce
