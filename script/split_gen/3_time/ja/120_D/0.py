def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.reverse()
    B.reverse()
    # Union-Find
    par = [i for i in range(N+1)]
    rank = [0] * (N+1)
    size = [1] * (N+1)
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
            return False
        elif rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    def same(x, y):
        return find(x) == find(y)
    # 初期状態の不便さ
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if same(i, j):
                continue
            ans += size[i] * size[j]
            unite(i, j)
    print(ans)
    for i in range(M-1):
        a = A[i]
        b = B[i]
        if same(a, b):
            continue
        ans -= size[find(a)] * size[find(b)]
        unite(a, b)
        print(ans)
