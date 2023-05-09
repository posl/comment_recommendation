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

if __name__ == '__main__':
    main()