Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
    ans = 0
    for u in range(N):
        for v in range(u+1, N):
            if v in E[u]:
                continue
            if all(u not in E[v] for v in E[u]):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    edge = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if j in edge[i]:
                continue
            else:
                if len(edge[i]) + len(edge[j]) == N-2:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if j not in G[i]:
                if (len(G[i])+len(G[j]))%2==0:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    u = [0]*M
    v = [0]*M
    for i in range(M):
        u[i],v[i] = map(int,input().split())
    ans = 0
    for i in range(M):
        for j in range(i+1,M):
            if u[i] == u[j] or u[i] == v[j] or v[i] == u[j] or v[i] == v[j]:
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    ans = 0
    for i in range(M):
        u, v = edges[i]
        u -= 1
        v -= 1
        for a in adj[u]:
            if a == v:
                continue
            for b in adj[v]:
                if b == u:
                    continue
                if a in adj[b]:
                    continue
                ans += 1
    print(ans // 6)
    return

=======
Suggestion 6

def main():
    import sys
    import numpy as np
    read = sys.stdin.buffer.read
    N, M, *UV = map(int, read().split())
    #N, M, *UV = map(int, input().split())
    #N, M, *UV = map(int, open(0).read().split())
    #N, M, *UV = map(int, open('problems282_d.txt').read().split())
    #N, M, *UV = map(int, open('problems282_d_1.txt').read().split())
    #N, M, *UV = map(int, open('problems282_d_2.txt').read().split())
    #N, M, *UV = map(int, open('problems282_d_3.txt').read().split())

    #N, M = 10**5,

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    edge.sort()
    # 連結成分の個数を求める
    # 連結成分の個数は、辺の個数 + 1 である
    # 連結成分の個数 - 1 を出力すればよい
    # 連結成分の個数が 2 つ以上ある場合、
    # 連結成分の個数 - 1 が答えとなる
    # 連結成分の個数が 1 つの場合、
    # 連結成分の個数 - 1 が答えとなる

    # 連結成分の個数を求める
    # 連結成分の個数は、辺の個数 + 1 である
    # 連結成分の個数 - 1 を出力すればよい
    # 連結成分の個数が 2 つ以上ある場合、
    # 連結成分の個数 - 1 が答えとなる
    # 連結成分の個数が 1 つの場合、
    # 連結成分の個数 - 1 が答えとなる

    # 連結成分の個数を求める
    # 連結成分の個数は、辺の個数 + 1 である
    # 連結成分の個数 - 1 を出力すればよい
    # 連結成分の個数が 2 つ以上ある場合、
    # 連結成分の個数 - 1 が答えとなる
    # 連結成分の個数が 1 つの場合、

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # 頂点の接続関係を記録
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # 頂点の色を記録
    color = [0] * (N+1)
    # 二部グラフか判定
    def dfs(v, c):
        color[v] = c
        for nv in graph[v]:
            if color[nv] == c:
                return False
            if color[nv] == 0 and not dfs(nv, -c):
                return False
        return True
    ans = 0
    for i in range(1, N+1):
        if color[i] == 0:
            if dfs(i, 1):
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    # まず、与えられたグラフを作成する
    # 二部グラフの条件を満たすグラフであることは保証されている
    # つまり、頂点 u と頂点 v を結ぶ辺が存在しない場合は、
    # 頂点 u と頂点 v は同じ色に塗られている
    # したがって、同じ色に塗られている頂点どうしを結ぶ辺が存在してはいけない
    # つまり、頂点 u と頂点 v を結ぶ辺が存在しない場合、
    # 頂点 u と頂点 v は同じグループに属するということになる
    # したがって、頂点 u と頂点 v を結ぶ辺が存在しない場合、
    # 頂点 u と頂点 v を結ぶ辺を追加して得られるグラフは二部グラフである
    # つまり、頂点 u と頂点 v を結ぶ辺が存在しない場合、
    # 頂点 u と頂点 v を結ぶ辺を追加して得られるグラフが二部グラフである
    # ということはない
    # つまり、頂点 u と頂点 v を結ぶ辺が存在しない場合、
    # 頂点 u と頂点 v を結ぶ辺を追加して得られるグラフが二部グラフではない
    # ということはない
    # つまり、頂点 u と頂点 v を結ぶ
