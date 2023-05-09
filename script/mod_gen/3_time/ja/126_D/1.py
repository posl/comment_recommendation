def main():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    ans = [-1] * n
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv, w in g[v]:
            if ans[nv] == -1:
                if w % 2 == 0:
                    ans[nv] = ans[v]
                else:
                    ans[nv] = 1 - ans[v]
                q.append(nv)
    for a in ans:
        print(a)
main()

if __name__ == '__main__':
    main()