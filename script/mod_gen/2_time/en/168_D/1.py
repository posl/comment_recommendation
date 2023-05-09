def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    ans = [-1] * n
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in g[v]:
            if ans[nv] == -1:
                ans[nv] = v
                q.append(nv)
    print('Yes')
    for a in ans[1:]:
        print(a + 1)
main()

if __name__ == '__main__':
    main()