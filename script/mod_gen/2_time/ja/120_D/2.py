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

if __name__ == '__main__':
    main()