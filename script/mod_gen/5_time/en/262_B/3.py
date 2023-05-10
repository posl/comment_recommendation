def solve():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].add(v)
        G[v].add(u)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if j not in G[i]:
                continue
            for k in range(j + 1, N):
                if k not in G[i]:
                    continue
                if k not in G[j]:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()