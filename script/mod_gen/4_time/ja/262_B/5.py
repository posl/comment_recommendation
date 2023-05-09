def solve():
    # N = 3
    # M = 1
    # U = [1]
    # V = [2]
    # N = 5
    # M = 6
    # U = [1, 4, 2, 1, 3, 2]
    # V = [5, 5, 3, 4, 5, 5]
    N = 7
    M = 10
    U = [1, 5, 2, 3, 4, 1, 2, 1, 1, 2]
    V = [7, 7, 5, 6, 7, 5, 4, 3, 6, 7]
    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[U[i]].append(V[i])
        G[V[i]].append(U[i])
    ans = 0
    for i in range(1, N+1):
        for j in G[i]:
            for k in G[j]:
                if k != i and k not in G[i]:
                    ans += 1
    print(ans//6)

if __name__ == '__main__':
    solve()