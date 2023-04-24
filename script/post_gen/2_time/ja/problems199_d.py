Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(3 ** N - (2 ** M))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3 ** N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    ans = 0
    for i in range(3 ** N):
        flag = True
        for j in range(N):
            for k in range(j + 1, N):
                if (i >> j & 1) == (i >> k & 1) and k in G[j]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
    else:
        print(0)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(3**n)
        return
    edges = [list(map(int, input().split())) for i in range(m)]
    #print(edges)
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[2][0])
    #print(edges[2][1])
    #print(edges[3][0])
    #print(edges[3][1])
    #print(edges[4][0])
    #print(edges[4][1])
    #print(edges[5][0])
    #print(edges[5][1])
    ans = 0
    for i in range(3**n):
        color = [0] * (n + 1)
        for j in range(n):
            color[j + 1] = (i // (3**j)) % 3
        #print(color)
        flag = 1
        for j in range(m):
            if color[edges[j][0]] == color[edges[j][1]]:
                flag = 0
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    edges = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a-1][b-1] = 1
        edges[b-1][a-1] = 1
    ans = 0
    for i in range(3**N):
        i = str(i).zfill(N)
        ok = True
        for j in range(N):
            for k in range(j+1, N):
                if i[j] == i[k] and edges[j][k] == 1:
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
    import sys
    read = sys.stdin.buffer.read
    N, M, *AB = map(int, read().split())
    if M == 0:
        print(3**N)
        return
    edge = [0] * N
    for a, b in zip(*(iter(AB),) * 2):
        edge[a - 1] |= 1 << (b - 1)
        edge[b - 1] |= 1 << (a - 1)
    dp = [0] * (1 << N)
    dp[0] = 1
    for i in range(1 << N):
        for j in range(N):
            if (i >> j) & 1:
                continue
            if i & edge[j] == 0:
                dp[i | (1 << j)] += dp[i]
    print(dp[-1] * 3)

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    #入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #辺の有無を判定するためのリスト
    edge = [[0] * N for _ in range(N)]
    for i in range(M):
        edge[AB[i][0] - 1][AB[i][1] - 1] = 1
        edge[AB[i][1] - 1][AB[i][0] - 1] = 1
    #print(edge)
    #頂点1から頂点Nまでの各頂点が赤、緑、青のいずれかで塗られている場合の数
    ans = 1
    for i in range(N):
        #頂点iから頂点i+1までの各頂点が赤、緑、青のいずれかで塗られている場合の数
        ans *= 3
    #print(ans)
    #頂点iから頂点i+1までの各頂点が赤、緑、青のいずれかで塗られている場合の数から、条件を満たさない場合の数を引く
    for i in range(N):
        for j in range(i + 1, N):
            if edge[i][j] == 1:
                #頂点iと頂点jが辺で直接結ばれている場合
                ans -= 3
    #print(ans)
    #頂点iと頂点jが辺で直接結ばれている場合の数を引く
    for i in range(M):
        for j in range(i + 1, M):
            if edge[AB[i][0] - 1][AB[j][0] - 1] == 1 and edge[AB[i][0] - 1][AB[j][1] - 1] == 1 and edge[AB[i][1] - 1][

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    
    n,m = map(int,input().split())
    if m == 0:
        print(3**n)
        return
    
    #辺のリストを作成
    edge = [list(map(int,input().split())) for _ in range(m)]
    
    #各頂点の隣接リストを作成
    adj = [[] for _ in range(n)]
    for a,b in edge:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    
    #頂点を赤、緑、青のいずれかで塗る
    #辺で直接結ばれている 2 頂点は必ず異なる色で塗られている
    #なお、使われない色があっても構いません。
    ans = 0
    #頂点iを赤で塗る場合
    for i in range(n):
        #頂点iに隣接している頂点を赤で塗ることはできない
        for j in adj[i]:
            if j < i:
                break
        else:
            #頂点iに隣接している頂点を緑で塗る場合
            for k in range(n):
                #頂点kに隣接している頂点を緑で塗ることはできない
                for l in adj[k]:
                    if l < k:
                        break
                else:
                    #頂点iと頂点kに隣接している頂点を青で塗る場合
                    for m in range(n):
                        #頂点mに隣接している頂点を青で塗ることはできない
                        for n in adj[m]:
                            if n < m:
                                break
                        else:
                            #頂点iと頂点kに隣接している頂点を青で塗ることはできる
