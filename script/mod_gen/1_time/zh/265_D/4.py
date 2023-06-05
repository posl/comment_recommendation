def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右累加A[i]，得到B[i]
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i - 1] + A[i]
    # 从右到左累加A[i]，得到C[i]
    C = [0] * N
    C[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        C[i] = C[i + 1] + A[i]
    # 从左到右累加B[i]，得到D[i]
    D = [0] * N
    D[0] = B[0]
    for i in range(1, N):
        D[i] = D[i - 1] + B[i]
    # 从右到左累加C[i]，得到E[i]
    E = [0] * N
    E[N - 1] = C[N - 1]
    for i in range(N - 2, -1, -1):
        E[i] = E[i + 1] + C[i]
    # 从左到右累加D[i]，得到F[i]
    F = [0] * N
    F[0] = D[0]
    for i in range(1, N):
        F[i] = F[i - 1] + D[i]
    # 从右到左累加E[i]，得到G[i]
    G = [0] * N
    G[N - 1] = E[N - 1]
    for i in range(N - 2, -1, -1):
        G[i] = G[i + 1] + E[i]
    # 检查是否存在满足条件的元组
    for i in range(1, N - 1):
        if B[i] == P and C[i] == Q and D[i] == P + Q and E[i] == Q + R and F[i]

if __name__ == '__main__':
    solve()