def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * (N+1)
    C = [0] * (N+1)
    D = [0] * (N+1)
    E = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    for i in range(N):
        C[i+1] = C[i] + A[i]
    for i in range(N):
        D[i+1] = D[i] + A[i]
    for i in range(N):
        E[i+1] = E[i] + A[i]
    for i in range(N):
        C[i+1] = max(C[i], C[i+1])
    for i in range(N):
        D[i+1] = max(D[i], D[i+1])
    for i in range(N):
        E[i+1] = max(E[i], E[i+1])
    for i in range(N):
        C[i+1] = min(C[i], C[i+1])
    for i in range(N):
        D[i+1] = min(D[i], D[i+1])
    for i in range(N):
        E[i+1] = min(E[i], E[i+1])
    ans = 10**9
    for i in range(1, N-1):
        b = B[i]
        c = C[i]
        d = D[i]
        e = E[i]
        ans = min(ans, max(b, c, d, e) - min(b, c, d, e))
    print(ans)

if __name__ == '__main__':
    solve()