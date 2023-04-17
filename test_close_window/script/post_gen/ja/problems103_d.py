Synthesizing 10/10 solutions

=======

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = 0
    for i in range(M):
        ans += 1
        for j in range(M):
            if A[j] == A[i] or B[j] == A[i] or A[j] == B[i] or B[j] == B[i]:
                A[j] = -1
                B[j] = -1

    print(ans)

main()

=======

def main():
    N, M = map(int, input().split())
    bridge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        bridge[a-1].append(b-1)
        bridge[b-1].append(a-1)
    print(N-1-M+dfs(0, bridge))

=======

def main():
    N, M = map(int, input().split())
    bridge = [set() for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        bridge[a-1].add(b-1)
        bridge[b-1].add(a-1)
    bridge = [sorted(list(x)) for x in bridge]
    #print(bridge)
    visited = [False] * N
    visited[0] = True
    remove = 0
    for i in range(N):
        if visited[i]:
            for j in bridge[i]:
                if not visited[j]:
                    visited[j] = True
                    remove += 1
    print(remove)

=======

def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append((a, b))
    bridges.sort()
    ans = 0
    for i, bridge in enumerate(bridges):
        if i == 0:
            ans += 1
            continue
        if bridges[i-1][1] < bridge[0]:
            ans += 1
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    bridge.sort(key=lambda x: x[1])
    ans = 0
    last_bridge = 0
    for a, b in bridge:
        if a <= last_bridge:
            continue
        ans += 1
        last_bridge = b-1
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    B = [0] * (N - 1)
    for i in range(M):
        a, b = map(int, input().split())
        B[min(a, b) - 1] += 1
    print(B.count(1))

=======

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        a, b = map(int, input().split())
        AB.append((a, b))

    # 橋がない場合は、全ての島が繋がっているので、全ての島が争いに巻き込まれる
    if N == M:
        print(N)
        return

    # 橋がある場合、島の番号の大小関係は、橋の番号の大小関係と一致する
    # 橋の番号の小さい方から順に、橋を取り除いていく
    # その際、橋を取り除いた後の島の繋がりを調べる
    # その際、繋がりのない島の組み合わせが、争いに巻き込まれた島の組み合わせと一致する
    # そのため、繋がりのない島の組み合わせの数をカウントする
    # その際、繋がりのない島の組み合わせの数が 1 以上の場合、橋を取り除いた後にも繋がりのない島が存在する
    # そのため、橋を取り除いた場合、争いに巻き込まれた島の組み合わせの数は、繋がりのない島の組み合わせの数より 1 大きくなる
    # そのため、繋がりのない島の組み合わせの数をカウントする
    # その際、繋がりのない島の組み合わせの数が

=======

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    # Union-Find
    class UnionFind:
        def __init__(self, n):
            self.par = list(range(n))
            self.rank = [0] * n
            self.size = [1] * n
        def root(self, x):
            if self.par[x] == x:
                return x
            else:
                self.par[x] = self.root(self.par[x])
                return self.par[x]
        def unite(self, x, y):
            x = self.root(x)
            y = self.root(y)
            if x == y:
                return
            elif self.rank[x] < self.rank[y]:
                self.par[x] = y
                self.size[y] += self.size[x]
            else:
                self.par[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
        def same(self, x, y):
            return self.root(x) == self.root(y)
        def size(self, x):
            return self.size[self.root(x)]

    uf = UnionFind(N)
    for a, b in AB:
        uf.unite(a-1, b-1)

    ans = 0
    for a, b in AB:
        if not uf.same(a-1, b-1):
            uf.unite(a-1, b-1)
            ans += 1
    print(ans)

=======

def main():
    #入力
    N, M = map(int, input().split())
    #N, M = 5, 2
    #N, M = 9, 5
    #N, M = 5, 10
    #要望
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        #a_i, b_i = 1, 4
        #a_i, b_i = 2, 7
        #a_i, b_i = 1, 2
        a.append(a_i)
        b.append(b_i)

    #グラフの構築
    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])

    #グラフの探索
    #1からの距離を記録する
    dist = [-1] * (N+1)
    dist[1] = 0
    #探索する島の番号を記録する
    que = [1]
    while que:
        v = que.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)

    #最大値を記録する
    max_dist = 0
    for i in range(1, N+1):
        max_dist = max(max_dist, dist[i])

    #最大値の数をカウントする
    cnt = 0
    for i in range(1, N+1):
        if dist[i] == max_dist:
            cnt += 1

    #答え
    print(max_dist, cnt)

=======

def main():
    N, M = map(int, input().split())
    #橋を取り除く必要があるかどうか
    bridge = [True] * (N-1)
    #橋を取り除いた時の連結成分の数
    cnt = [0] * (N-1)
    #連結成分の数
    cc = N-1
    for i in range(M):
        a, b = map(int, input().split())
        #橋を取り除く
        if bridge[a-1]:
            bridge[a-1] = False
            cc -= 1
        #橋を取り除く
        if bridge[b-2]:
            bridge[b-2] = False
            cc -= 1
        #連結成分の数を更新
        cnt[a-1] = cc
        cnt[b-2] = cc
    #連結成分の数が最小の橋を取り除く
    print(cnt.index(min(cnt))+1)
