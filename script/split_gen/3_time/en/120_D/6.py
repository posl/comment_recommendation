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
