def main():
    N, M = map(int, input().split())
    if N == 2:
        if M == 0:
            print(0)
        else:
            print(1)
        return
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)
    MOD = 10**9 + 7
    D = [0] * (N + 1)
    D[1] = 1
    Q = [1]
    while Q:
        n = Q.pop()
        for m in G[n]:
            if D[m] == 0:
                D[m] = D[n] + 1
                Q.append(m)
    if D[N] == 0:
        print(0)
        return
    P = [0] * (N + 1)
    P[N] = 1
    Q = [N]
    while Q:
        n = Q.pop()
        for m in G[n]:
            if D[m] == D[n] - 1:
                P[m] = (P[m] + P[n]) % MOD
                Q.append(m)
    print(P[1])
