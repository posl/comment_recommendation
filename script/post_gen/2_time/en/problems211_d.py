Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    dist = [-1] * N
    dist[0] = 0
    queue = [0]
    while queue:
        v = queue.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    if dist[-1] == -1:
        print(0)
        return
    ans = 0
    mod = 10**9 + 7
    dp = [0] * N
    dp[0] = 1
    for d in range(1, dist[-1]+1):
        for v in range(N):
            if dist[v] == d:
                for nv in G[v]:
                    if dist[nv] == d-1:
                        dp[v] += dp[nv]
                        dp[v] %= mod
    print(dp[-1])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    mod = 10 ** 9 + 7

    def bfs():
        q = [0]
        dist = [-1] * N
        dist[0] = 0
        cnt = [0] * N
        cnt[0] = 1
        while q:
            v = q.pop()
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    q.append(nv)
                if dist[nv] == dist[v] + 1:
                    cnt[nv] += cnt[v]
                    cnt[nv] %= mod
        return cnt[N - 1]

    print(bfs())

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    MOD = 10 ** 9 + 7
    dist = [-1] * N
    dist[0] = 0
    from collections import deque
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[-1] == -1:
        print(0)
        return
    ans = 1
    for i in range(1, N):
        cnt = 0
        for v in G[i]:
            if dist[v] == dist[i] - 1:
                cnt += 1
        ans = ans * cnt % MOD
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    MOD = 10 ** 9 + 7
    from collections import deque
    Q = deque([0])
    dist = [-1] * N
    dist[0] = 0
    cnt = [0] * N
    cnt[0] = 1
    while Q:
        v = Q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                cnt[nv] = cnt[v]
                Q.append(nv)
            elif dist[nv] == dist[v] + 1:
                cnt[nv] += cnt[v]
                cnt[nv] %= MOD
    print(cnt[N - 1])

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        E[a].append(b)
        E[b].append(a)
    MOD = 10**9 + 7

    # dp[i]: i番目の都市にいるときのパスの数
    dp = [0] * N
    dp[0] = 1
    for i in range(N-1):
        for j in E[i]:
            dp[j] += dp[i]
            dp[j] %= MOD
    print(dp[N-1])
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    ans = 0
    for i in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    flag = [0] * N
    flag[0] = 1
    queue = [[0, 1]]
    while queue:
        now, cnt = queue.pop()
        if now == N-1:
            ans += cnt
            ans %= (10**9 + 7)
            continue
        for i in graph[now]:
            if flag[i] == 0:
                flag[i] = 1
                queue.append([i, cnt])
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[1])
    print(edges)
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for a, b in edges:
            if i == a:
                dp[b] += dp[a]
            if i == b:
                dp[a] += dp[b]
    print(dp[N] % (10 ** 9 + 7))

=======
Suggestion 8

def find_shortest_path(N, M, A, B):
    # initialize graph
    graph = [[] for _ in range(N)]
    for a, b in zip(A, B):
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # initialize distance
    distance = [-1] * N
    distance[0] = 0

    # initialize queue
    queue = [0]

    # initialize path
    path = [0] * N
    path[0] = 1

    while queue:
        current = queue.pop(0)
        for next in graph[current]:
            if distance[next] == -1:
                distance[next] = distance[current] + 1
                queue.append(next)
                path[next] = path[current]
            elif distance[next] == distance[current] + 1:
                path[next] += path[current]
                path[next] %= 1000000007

    return path[N-1]

=======
Suggestion 9

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
