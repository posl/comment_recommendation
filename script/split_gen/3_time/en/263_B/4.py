def solve():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    G = [0] * (N + 1)
    for i in range(1, N + 1):
        G[i] = G[P[i]] + 1
    print(max(G))
