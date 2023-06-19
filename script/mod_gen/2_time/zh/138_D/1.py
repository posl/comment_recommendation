def main():
    N, Q = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    P = [0]*N
    for _ in range(Q):
        p, x = map(int, input().split())
        P[p-1] += x
    ans = [0]*N
    def dfs(v, p):
        ans[v] = P[v]
        for nv in E[v]:
            if nv == p:
                continue
            P[nv] += P[v]
            dfs(nv, v)
    dfs(0, -1)
    print(*ans)

if __name__ == '__main__':
    main()