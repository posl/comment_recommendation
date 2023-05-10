def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    D = [0] * (N + 1)
    E = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
        C[i + 1] = C[i] + A[i]
        D[i + 1] = D[i] + A[i]
        E[i + 1] = E[i] + A[i]
    for i in range(N):
        B[i + 1] = max(B[i + 1], B[i])
    for i in range(N):
        C[i + 1] = min(C[i + 1], C[i])
    for i in range(N):
        D[i + 1] = max(D[i + 1], D[i])
    for i in range(N):
        E[i + 1] = min(E[i + 1], E[i])
    ans = 10 ** 18
    for i in range(1, N - 1):
        ans = min(ans, abs(B[i] - C[i]) + abs(D[i] - E[i + 1]))
    print(ans)

if __name__ == '__main__':
    solve()