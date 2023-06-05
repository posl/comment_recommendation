def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    R = [0] * N
    R[0] = 1
    S = [0]
    while S:
        x = S.pop()
        for y in G[x]:
            if R[y] == 0:
                R[y] = x + 1
                S.append(y)
    print('Yes')
    print('\n'.join(map(str, R[1:])))
solve()
