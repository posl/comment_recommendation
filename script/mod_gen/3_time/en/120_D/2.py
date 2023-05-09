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

if __name__ == '__main__':
    main()