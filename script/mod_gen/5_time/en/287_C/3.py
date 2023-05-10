def solve():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    for u in range(N):
        if len(G[u]) > 2:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()