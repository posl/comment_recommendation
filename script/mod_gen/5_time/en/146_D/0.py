def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    used = [False] * n
    ans = [0] * (n - 1)
    def dfs(v, p):
        c = 1
        for u in tree[v]:
            if u == p:
                continue
            if c == ans[v]:
                c += 1
            ans[u] = c
            c += 1
            dfs(u, v)
    dfs(0, -1)
    print(max(ans))
    for c in ans:
        print(c)

if __name__ == '__main__':
    main()