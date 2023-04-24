Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各島について、島に到達するために必要な橋の本数を記録
    bridge = [0] * (N+1)
    #各

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    #print(G)
    ans = [N*(N-1)//2]
    for i in range(M-1, -1, -1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if len(G[a]) > len(G[b]):
            a, b = b, a
        #print(a, b)
        G[a].remove(b)
        G[b].remove(a)
        ans.append(ans[-1] - len(G[a]))
        for c in G[a]:
            G[c].remove(a)
            G[c].add(b)
            G[b].add(c)
        G[a] = set()
    for i in range(M, -1, -1):
        print(ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    bridge = bridge[::-1]
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    #print(ans)
    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)
    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]
        ans[0] -= size[y] * (size[y] - 1) // 2
    for i in range(1, M):
        a, b = bridge[i]
        if find(a) != find(b):
            ans[i] = ans[i - 1] - size[find(a)] * size[find(b)]
            unite(a, b)
        else:
            ans[i] = ans[i - 1]
    for i in range(M):
        print(ans[M - i - 1])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)
    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            if size[x] < size[y]:
                x, y = y, x
            parent[y] = x
            size[x] += size[y]
            ans[0] -= size[y] * (size[y] - 1) // 2
    for i in range(1, M):
        a, b = bridges[i]
        ans[i] = ans[i - 1]
        if find(a) != find(b):
            ans[i] -= size[find(a)] * size[find(b)]
            unite(a, b)
    ans.reverse()
    print(*ans, sep='

')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    par = [i for i in range(N+1)]
    rank = [0 for i in range(N+1)]
    for i in range(1, M):
        a, b = AB[i]
        ans[i] = ans[i-1] - union(a, b, par, rank)
    ans.reverse()
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a, b = zip(*[map(int, input().split()) for _ in range(m)])
    a = [a_ - 1 for a_ in a]
    b = [b_ - 1 for b_ in b]

    # 連結成分
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i], b[i])

    # 連結成分ごとに島の数を数える
    islands = [0] * n
    for i in range(n):
        islands[uf.root(i)] += 1

    # 連結成分の島の数の和を計算する
    sums = [0] * n
    for i in range(n):
        sums[uf.root(i)] += islands[i]

    # 連結成分ごとに不便さを計算する
    ans = [0] * m
    for i in range(m - 1, -1, -1):
        ans[i] = sums[uf.root(a[i])] * sums[uf.root(b[i])]
        sums[uf.root(a[i])] = 0
        sums[uf.root(b[i])] = 0

    # 累積和を計算する
    for i in range(1, m):
        ans[i] += ans[i - 1]

    for i in range(m):
        print(ans[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(bridge)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print(island)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print(island)
    #print()
    #橋の数だけのリストを作る
    bridge_list = [0] * M
    #print(bridge_list)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print(island)
    #print()
    #橋の数だけのリストを作る
    bridge_list = [0] * M
    #print(bridge_list)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print(island)
    #print()
    #橋の数だけのリストを作る
    bridge_list = [0] * M
    #print(bridge_list)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print(island)
    #print()
    #橋の数だけのリストを作る
    bridge_list = [0] * M
    #print(bridge_list)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print(island)
    #print()
    #橋の数だけのリストを作る
    bridge_list = [0] * M
    #print(bridge_list)
    #print()
    #島の数だけのリストを作る
    island = [0] * (N + 1)
    #print

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    bridge = [tuple(map(int, input().split())) for _ in range(M)]
    #print(bridge)
    #print(N, M)
    #print(bridge)
    #print(bridge[0][0])
    #print(bridge[0][1])

    #不便さの初期値は0
    inconvenience = 0
    #島の数を初期化
    island = [0] * (N + 1)
    #島の数の初期値は1
    for i in range(1, N + 1):
        island[i] = 1
    #print(island)

    #橋の個数を初期化
    bridge_num = [0] * (N + 1)
    #橋の個数の初期値は0
    for i in range(1, N + 1):
        bridge_num[i] = 0
    #print(bridge_num)

    #不便さの初期値を計算
    for i in range(1, N + 1):
        inconvenience += (island[i] * (island[i] - 1)) // 2
    #print(inconvenience)

    #不便さを出力
    print(inconvenience)

    #橋の個数を計算
    for i in range(M):
        bridge_num[bridge[i][0]] += 1
        bridge_num[bridge[i][1]] += 1
    #print(bridge_num)

    #橋の個数を用いて不便さを計算
    for i in range(M):
        inconvenience -= (island[bridge[i][0]] * (island[bridge[i][0]] - 1)) // 2
        inconvenience -= (island[bridge[i][1]] * (island[bridge[i][1]] - 1)) // 2
        island[bridge[i][0]] += 1
        island[bridge[i][1]] += 1
        inconvenience += (island[bridge[i][0]] * (island[bridge[i][0]] - 1)) // 2
