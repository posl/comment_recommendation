def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    for i in range(N):
        if len(G[i]) > 2:
            print("No")
            return
    print("Yes")
    return
