def main():
    n, m = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(m)]
    bridge.reverse()
    ans = [0] * m
    ans[0] = n * (n - 1) // 2
    uf = UnionFind(n)
    for i, (a, b) in enumerate(bridge):
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i + 1] = ans[i]
        else:
            ans[i + 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.union(a, b)
    ans.reverse()
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()