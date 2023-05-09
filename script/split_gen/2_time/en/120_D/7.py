def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    # 1-indexed
    par = list(range(N + 1))
    rank = [0] * (N + 1)
    size = [1] * (N + 1)
    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            x, y = y, x
        if rank[x] == rank[y]:
            rank[x] += 1
        par[y] = x
        size[x] += size[y]
    def same(x, y):
        return find(x) == find(y)
    def get_size(x):
        return size[find(x)]
    ans = [0] * M
    ans[-1] = N * (N - 1) // 2
    for i in range(M - 1, 0, -1):
        a, b = bridges[i]
        if same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - get_size(a) * get_size(b)
            unite(a, b)
    for i in range(M):
        print(ans[i])
