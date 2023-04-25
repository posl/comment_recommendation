Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)

    # 橋の破壊順を逆にする
    A.reverse()
    B.reverse()

    # 累積和を計算する
    # 累積和の初期値は、全ての橋を通れる状態
    # つまり、全ての島の親は同じで、同じグループに属している
    # そのため、累積和は、最初はNをM個分追加して、M個分引く
    # これで、最初のグループの数を計算できる
    # その後、各島の親を更新していく
    group = [N] * (M + 1)
    for i in range(M):
        group[i + 1] = group[i] + 1 - group[i + 1]
    #print(group)

    # 連結成分の個数
    # 連結成分の個数を数えるために、Union Findを使う
    # 連結成分の個数を数えるには、
    # 1. 連結成分の個数を数える
    # 2. 橋を破壊する
    # 3. 連結成分の個数を数える
    # 4. 2. 3. を繰り返す
    # という流れになる
    # 1. 連結成分の個数を数える
    # 連結成分の個数を数えるには、
    # 1.1. 最初は各島

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0 for _ in range(M)]
    ans[M-1] = (N-1)*N//2
    par = [i for i in range(N+1)]
    size = [1 for _ in range(N+1)]
    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        par[y] = x
        size[x] += size[y]
        return True
    for i in range(M-1, 0, -1):
        ans[i-1] = ans[i]
        if unite(A[i], B[i]):
            ans[i-1] -= size[root(A[i])]*size[root(B[i])]
    for i in range(M):
        print(ans[i])

=======
Suggestion 3

def main():
    N, M = [int(x) for x in input().split()]
    bridges = []
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        bridges.append((a, b))
    bridges.reverse()

    # Union-Find
    p = [i for i in range(N + 1)]
    def root(x):
        if p[x] == x:
            return x
        p[x] = root(p[x])
        return p[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        p[x] = y

    ans = []
    n = N * (N - 1) // 2
    for a, b in bridges:
        ans.append(n)
        if root(a) != root(b):
            n -= (root(a) - 1) * (root(b) - 1)
            unite(a, b)
    ans.reverse()
    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append((min(a, b), max(a, b)))
    bridges = bridges[::-1]

    # disjoint set
    parent = [i for i in range(N + 1)]
    size = [1 for _ in range(N + 1)]
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
        return

    # count
    count = 0
    for i in range(1, N + 1):
        count += size[find(i)] - 1
    for i in range(M):
        print(count)
        a, b = bridges[i]
        if find(a) != find(b):
            count -= size[find(a)] * size[find(b)]
            unite(a, b)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.reverse()
    ans = [n * (n - 1) // 2]
    uf = UnionFind(n)
    for a, b in ab:
        a -= 1
        b -= 1
        ans.append(ans[-1] - uf.size(a) * uf.size(b))
        uf.unite(a, b)
    for a in ans[:-1][::-1]:
        print(a)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]

    parent = list(range(N + 1))
    size = [1] * (N + 1)
    cnt = [0] * (N + 1)
    ans = [0] * M

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        parent[x] = y
        size[y] += size[x]
        cnt[y] += cnt[x]

    for i in range(M - 1, -1, -1):
        a, b = bridges[i]
        ans[i] = N * (N - 1) // 2 - (N - size[find(a)]) * (N - size[find(b)])
        union(a, b)
        N -= 1

    print('

'.join(map(str, ans)))

main()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    ans = [0] * M
    ans[-1] = N * (N - 1) // 2

    parent = list(range(N + 1))
    size = [1] * (N + 1)

    def root(x):
        if parent[x] == x:
            return x
        parent[x] = root(parent[x])
        return parent[x]

    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]
        return True

    for i in range(M - 1, 0, -1):
        ans[i - 1] = ans[i]
        if unite(AB[i][0], AB[i][1]):
            ans[i - 1] -= size[root(AB[i][0])] * size[root(AB[i][1])]

    for i in range(M):
        print(ans[i])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.reverse()
    par = [i for i in range(N+1)]
    size = [1 for i in range(N+1)]
    ans = [0 for i in range(M)]
    now = N*(N-1)//2
    for i in range(M):
        a, b = AB[i]
        if find(par, a) != find(par, b):
            now -= size[find(par, a)]*size[find(par, b)]
            unite(par, size, a, b)
        ans[i] = now
    ans.reverse()
    for i in range(M):
        print(ans[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    uf = UnionFind(N)
    for i, (a, b) in enumerate(bridges):
        if i == 0:
            continue
        ans[i] = ans[i - 1]
        if uf.same(a - 1, b - 1):
            continue
        ans[i] -= uf.size(a - 1) * uf.size(b - 1)
        uf.union(a - 1, b - 1)
    print('

'.join(map(str, ans[::-1])))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0 for _ in range(M)]
    ans[0] = N * (N - 1) // 2
    cnt = [1 for _ in range(N + 1)]
    for i in range(1, M):
        a, b = AB[i - 1]
        ans[i] = ans[i - 1]
        if cnt[a] > cnt[b]:
            a, b = b, a
        if cnt[a] > 0:
            ans[i] -= cnt[a] * (cnt[a] - 1) // 2
        if cnt[b] > 0:
            ans[i] -= cnt[b] * (cnt[b] - 1) // 2
        cnt[a] += cnt[b]
        cnt[b] = 0
        if cnt[a] > 0:
            ans[i] += cnt[a] * (cnt[a] - 1) // 2
    ans.reverse()
    for i in range(M):
        print(ans[i])
