def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + B[i]
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + A[i]
    E = [0] * (N + 1)
    for i in range(N):
        E[i + 1] = E[i] + (B[N // 2] - B[i])
    F = [0] * (N + 1)
    for i in range(N):
        F[i + 1] = F[i] + (B[N // 2 - 1] - B[i])
    G = [0] * (N + 1)
    for i in range(N):
        G[i + 1] = G[i] + (A[i] - B[N // 2])
    H = [0] * (N + 1)
    for i in range(N):
        H[i + 1] = H[i] + (A[i] - B[N // 2 - 1])
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i) * (i + 1)
    for i in range(N):
        ans -= (C[i + 1] + D[N] - D[i + 1]) * (N - i)
        ans -= (C[N] - C[i + 1] + D[N] - D[i + 1]) * (i + 1)
        ans += (E[i + 1] + F[N] - F[i + 1]) * (N - i)
        ans += (E[N] - E[i + 1] + F[N] - F[i + 1]) * (i + 1)
        ans -= (G[i + 1] + H[N] - H[i + 1]) * (N - i)
        ans -= (G[N] - G[i + 1] + H[N] - H[i + 1]) * (i + 1)
    print(ans // (2 * N))
