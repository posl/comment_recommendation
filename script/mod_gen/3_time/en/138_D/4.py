def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    counter = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    ans = [0] * n
    def dfs(v, p):
        ans[v] += counter[v]
        if p != -1:
            ans[v] += ans[p]
        for u in tree[v]:
            if u == p:
                continue
            dfs(u, v)
    dfs(0, -1)
    print(*ans)

if __name__ == '__main__':
    main()