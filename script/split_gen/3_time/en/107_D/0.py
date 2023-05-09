def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + A[i] * A[i]
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + A[i] * A[i] * A[i]
    E = [0] * (N + 1)
    for i in range(N):
        E[i + 1] = E[i] + A[i] * A[i] * A[i] * A[i]
    ans = 0
    for i in range(N):
        l, r = 0, N
        while r - l > 1:
            m = (l + r) // 2
            if (B[m] - B[i]) * (B[m] - B[i]) * (B[m] - B[i]) * (B[m] - B[i]) - 4 * (C[m] - C[i]) * (E[m] - E[i]) >= 0:
                r = m
            else:
                l = m
        ans += (B[r] - B[i]) * (B[r] - B[i]) * (B[r] - B[i]) * (B[r] - B[i]) - 3 * (C[r] - C[i]) * (D[r] - D[i]) - (C[r] - C[i]) * (C[r] - C[i]) * (E[r] - E[i])
        l, r = 0, N
        while r - l > 1:
            m = (l + r) // 2
            if (B[m] - B[i]) * (B[m] - B[i]) * (B[m] - B[i]) * (B[m] - B[i]) - 4 * (C[m] - C[i]) * (E[m] - E[i]) > 0:
                r = m
            else:
                l = m
        ans -= (B[r
