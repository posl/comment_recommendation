def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    for i in range(N):
        if len(G[i]) > 2:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()