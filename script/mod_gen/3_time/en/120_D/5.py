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
