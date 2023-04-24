Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    road = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        road[A-1].append(B-1)
        road[B-1].append(A-1)
    ans = [0 for i in range(N)]
    ans[0] = 1
    for i in range(N):
        for j in road[i]:
            ans[j] += ans[i]
            ans[j] %= 10**9 + 7
    print(ans[N-1])

=======
Suggestion 2

def main():
    import sys
    from collections import deque
    def input(): return sys.stdin.readline().strip()
    def list2d(a, b, c): return [[c] * b for i in range(a)]
    def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
    def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
    def ceil(x, y=1): return int(-(-x // y))
    def INT(): return int(input())
    def MAP(): return map(int, input().split())
    def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
    def Yes(): print('Yes')
    def No(): print('No')
    def YES(): print('YES')
    def NO(): print('NO')
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 18
    MOD = 10 ** 9 + 7

    N, M = MAP()
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = MAP()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    # 1からの距離と1からの道の数
    dist = [-1] * N
    dist[0] = 0
    cnt = [0] * N
    cnt[0] = 1
    Q = deque([0])
    while Q:
        v = Q.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            cnt[nv] = cnt[v]
            Q.append(nv)
        for nv in G[v]:
            if dist[nv] == dist[v] + 1:
                cnt[nv] += cnt[v]
                cnt[nv] %= MOD

    print(cnt[-1])

=======
Suggestion 3

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    mod = 10**9 + 7
    n, m = map(int, input().split())
    if m == 0:
        print(0)
        return
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    dist = [-1]*n
    dist[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[n-1] == -1:
        print(0)
        return
    dp = [0]*n
    dp[n-1] = 1
    for i in range(n-2, -1, -1):
        for nv in g[i]:
            if dist[nv] == dist[i] + 1:
                dp[i] += dp[nv]
                dp[i] %= mod
    print(dp[0])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if N == 2:
        print(0)
        return
    from collections import defaultdict
    d = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    #print(d)
    import heapq
    q = []
    heapq.heappush(q, (0, 1))
    visited = set()
    visited.add(1)
    while q:
        cost, node = heapq.heappop(q)
        if node == N:
            print(cost)
            return
        for n in d[node]:
            if n not in visited:
                visited.add(n)
                heapq.heappush(q, (cost+1, n))
    print(0)

=======
Suggestion 5

def main():
    import sys
    from collections import deque
    N, M = map(int, input().split())
    if N == 2:
        print(1)
        sys.exit()
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    q = deque()
    q.append(1)
    d = [0] * (N + 1)
    d[1] = 1
    while q:
        v = q.popleft()
        for w in G[v]:
            if d[w] == 0:
                d[w] = d[v] + 1
                q.append(w)
    ans = 0
    for v in G[N]:
        if d[v] == d[N] - 1:
            ans += 1
    print(ans % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)
    N, M = map(int, input().split())
    d = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    dist = [-1] * (N + 1)
    dist[1] = 0
    mod = 10**9 + 7
    ans = [0] * (N + 1)
    ans[1] = 1
    def dfs(v):
        for nv in d[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                ans[nv] = ans[v]
                dfs(nv)
            elif dist[nv] == dist[v] + 1:
                ans[nv] += ans[v]
                ans[nv] %= mod
    dfs(1)
    print(ans[N])

=======
Suggestion 7

def dijkstra(n, s, edges):
    import heapq
    from collections import defaultdict
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    dist = [float('inf')] * n
    dist[s] = 0
    que = [(0, s)]
    while que:
        d, v = heapq.heappop(que)
        if d > dist[v]:
            continue
        for nv, w in g[v]:
            if dist[nv] > d + w:
                dist[nv] = d + w
                heapq.heappush(que, (d + w, nv))
    return dist

=======
Suggestion 8

def main():
    # input
    N, M = map(int, input().split())
    # N = 2×10^5
    # M = 2×10^5
    # 1 ≦ A_i < B_i ≦ N
    # The pairs (A_i, B_i) are distinct.
    # All values in input are integers.
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    # print(roads)

    # N = 2×10^5
    # M = 2×10^5
    # 1 ≦ A_i < B_i ≦ N
    # The pairs (A_i, B_i) are distinct.
    # All values in input are integers.
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    # print(roads)

    # initialize
    # N = 2×10^5
    # M = 2×10^5
    # 1 ≦ A_i < B_i ≦ N
    # The pairs (A_i, B_i) are distinct.
    # All values in input are integers.
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    # print(roads)

    # process
    # N = 2×10^5
    # M = 2×10^5
    # 1 ≦ A_i < B_i ≦ N
    # The pairs (A_i, B_i) are distinct.
    # All values in input are integers.
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    # roads = [tuple(map(int, input().split())) for _ in range(M)]
    # print(roads)

    # output
    # N = 2×10^5
    # M = 2×10^5
    # 1 ≦ A_i < B_i ≦ N
    # The pairs (A_i, B_i) are distinct.
    # All values

=======
Suggestion 9

def main():
    #read the input
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #sort the input
    AB.sort(key=lambda x: x[0])
    #create a list of lists for the paths
    paths = [[] for _ in range(N)]
    for i in range(M):
        paths[AB[i][0] - 1].append(AB[i][1])
        paths[AB[i][1] - 1].append(AB[i][0])
    #create a list of lists for the distances
    dists = [[0 for _ in range(N)] for _ in range(N)]
    #create a list of lists for the counts
    counts = [[0 for _ in range(N)] for _ in range(N)]
    #initialize the first row of the counts
    counts[0] = [1 for _ in range(N)]
    #initialize the first row of the distances
    dists[0] = [1 for _ in range(N)]
    #initialize the visited list
    visited = [False for _ in range(N)]
    #initialize the queue
    queue = []
    #initialize the first element of the queue
    queue.append(1)
    #initialize the first element of the visited
    visited[0] = True
    #while the queue is not empty
    while queue:
        #get the next element
        node = queue.pop(0)
        #for each of the paths of the current node
        for i in range(len(paths[node - 1])):
            #if the node has not been visited
            if not visited[paths[node - 1][i] - 1]:
                #set the distance to the current node + 1
                dists[node - 1][paths[node - 1][i] - 1] = dists[node - 1][node - 1] + 1
                #set the count to the current node
                counts[node - 1][paths[node - 1][i] - 1] = counts[node - 1][node - 1]
                #set the visited flag to true
                visited[paths[node - 1][i] - 1] = True
                #add the node to the queue
                queue.append(paths[node

=======
Suggestion 10

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
