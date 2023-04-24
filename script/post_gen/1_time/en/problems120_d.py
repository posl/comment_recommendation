Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * M
    ans[M - 1] = (N - 1) * N // 2
    par = [0] * (N + 1)
    rank = [0] * (N + 1)
    for i in range(1, N + 1):
        par[i] = i
        rank[i] = 0
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return find(x) == find(y)
    for i in range(M - 1, 0, -1):
        ans[i - 1] = ans[i]
        if not same(A[i], B[i]):
            ans[i - 1] -= (rank[find(A[i])] + 1) * (rank[find(B[i])] + 1)
            unite(A[i], B[i])
    for i in range(M):
        print(ans[i])

=======
Suggestion 2

def main():
    N, M = [int(x) for x in input().split()]
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = [int(x) for x in input().split()]

    # Find the number of bridges between each pair of islands
    # (1, 2) and (2, 1) are considered the same.
    # The number of bridges between (i, j) is denoted by bridges[i][j].
    bridges = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        bridges[A[i]][B[i]] += 1
        bridges[B[i]][A[i]] += 1

    # Find the number of pairs of islands (a, b) (a < b) that we can travel between using some of the bridges remaining.
    # The number of pairs is denoted by pairs[i][j].
    pairs = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            pairs[i][j] = pairs[i][j - 1] + bridges[i][j]

    # Find the number of pairs of islands (a, b) (a < b) that we can travel between using some of the bridges remaining.
    # The number of pairs is denoted by pairs[i][j].
    pairs = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            pairs[i][j] = pairs[i][j - 1] + bridges[i][j]

    # Find the inconvenience just after the i-th bridge collapses.
    # The inconvenience is denoted by inconvenience[i].
    inconvenience = [0] * (M + 1)
    for i in range(1, M + 1):
        inconvenience[i] = inconvenience[i - 1] + pairs[A[i - 1]][B[i - 1]]

    # Print the inconvenience just after the i-th bridge collapses.
    for i in range(1, M

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    bridges = []
    for i in range(M):
        a, b = map(int, input().split())
        bridges.append((a, b))
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    #print(ans)
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    #print(parent, rank)
    def root(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = root(parent[x])
            return parent[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return root(x) == root(y)
    for i in range(M - 1):
        a, b = bridges[i]
        if same(a, b):
            ans[i + 1] = ans[i]
        else:
            ans[i + 1] = ans[i] - (rank[root(a)] + 1) * (rank[root(b)] + 1)
            unite(a, b)
    ans.reverse()
    for i in ans:
        print(i)
main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    uf = UnionFind(N)
    for i in range(1, M):
        a, b = AB[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] - uf.size(a) * uf.size(b)
            uf.unite(a, b)
    for i in range(M - 1, -1, -1):
        print(ans[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    count = [0] * (N + 1)
    for i in range(1, M):
        a, b = bridges[i - 1]
        if count[a] > count[b]:
            a, b = b, a
        ans[i] = ans[i - 1] - count[a]
        count[a] += 1
        count[b] += 1
    ans.reverse()
    for i in range(M):
        print(ans[i])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]
    bridge = bridge[::-1]
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    for i in range(1, M):
        if bridge[i][0] < bridge[i][1]:
            bridge[i][0], bridge[i][1] = bridge[i][1], bridge[i][0]
        if bridge[i] == bridge[i - 1]:
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] - 1
    for i in range(M):
        print(ans[M - 1 - i])

main()

This is my submission.

This code is very slow.

I'm not sure why this code is slow.

I think this code is O(N + M).

I think this is a problem with the input.

I tried to make a list of the number of bridges that connect the island.

However, it was not possible to pass the test.

I think this code is O(N + M).

I think this is a problem with the input.

I tried to make a list of the number of bridges that connect the island.

However, it was not possible to pass the test.

This is my submission.

This code is very slow.

I'm not sure why this code is slow.

I think this code is O(N + M).

I think this is a problem with the input.

I tried to make a list of the number of bridges that connect the island.

However, it was not possible to pass the test.

I think this code is O(N + M).

I think this is a problem with the input.

I tried to make a list of the number of bridges that connect the island.

However, it was not possible to pass the test.

I think this code is O(N + M).

I think this is a problem with the input.

I tried to make a list of the number of bridges that connect the island.

However, it was not possible to pass the test.

I think this code is O(N + M).

I think this is a problem with the input.

I tried to make a list of the number of bridges that connect the island.

However, it was not possible to pass the test.

I think this code is

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 連結成分の個数を管理する
    # 初期状態では全てが連結成分に分かれている
    root = [i for i in range(N + 1)]
    rank = [0 for i in range(N + 1)]
    size = [1 for i in range(N + 1)]

    # 連結成分の個数を返す
    def find(x):
        if root[x] == x:
            return x
        else:
            root[x] = find(root[x])
            return root[x]

    # xとyが同じ連結成分に属するか判定する
    def same(x, y):
        return find(x) == find(y)

    # xとyが属する連結成分を併合する
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            root[x] = y
            size[y] += size[x]
        else:
            root[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1

    # 残りの橋の個数を管理する
    # 初期状態では全ての橋が残っている
    remain = [1 for _ in range(M)]

    # 残りの橋の個数を返す
    def count(x):
        return remain[x]

    # 残りの橋の個数を1つ減らす
    def remove(x):
        remain[x] -= 1

    # 残りの橋の個数を返す
    def count(x):
        return remain[x]

    # 残りの橋の個数を1つ減らす
    def remove(x):
        remain[x] -= 1

    # 残

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    bridge = [tuple(map(int, input().split())) for i in range(M)]
    bridge.reverse()
    #print(bridge)
    ans = [0]*M
    ans[0] = N*(N-1)//2
    parent = [i for i in range(N+1)]
    size = [1]*(N+1)
    for i in range(1, M):
        a, b = bridge[i-1]
        if parent[a] == parent[b]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] - size[parent[a]]*size[parent[b]]
            if size[parent[a]] > size[parent[b]]:
                a, b = b, a
            size[parent[b]] += size[parent[a]]
            parent[a] = parent[b]
    ans.reverse()
    for i in range(M):
        print(ans[i])

main()

=======
Suggestion 9

def main():
    N, M = [int(x) for x in input().split()]
    bridges = [tuple(int(x) for x in input().split()) for i in range(M)]
    bridges.reverse()

    # Union-Find Tree
    root = [i for i in range(N + 1)]
    size = [1 for i in range(N + 1)]

    def find(x):
        if root[x] == x:
            return x
        else:
            root[x] = find(root[x])
            return root[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]
        return True

    # 結合前の不便さ
    inconvenience = sum((size[i] * (size[i] - 1)) // 2 for i in range(1, N + 1))
    print(inconvenience)

    for a, b in bridges:
        if unite(a, b):
            inconvenience -= (size[find(a)] * (size[find(a)] - 1)) // 2
            inconvenience -= (size[find(b)] * (size[find(b)] - 1)) // 2
        print(inconvenience)

=======
Suggestion 10

def main():
    #input
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    #solve
    # DSU
    par = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]
    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]
    def unite(x, y):
        rx = root(x)
        ry = root(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            par[rx] = ry
        else:
            par[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
    def same(x, y):
        return root(x) == root(y)

    # bridge
    ans = [0 for _ in range(M)]
    ans[M-1] = N*(N-1)//2
    for i in range(M-1, 0, -1):
        a, b = AB[i]
        if same(a, b):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - (rank[root(a)]+1)*(rank[root(b)]+1)
            unite(a, b)
    #output
    for i in range(M):
        print(ans[i])
