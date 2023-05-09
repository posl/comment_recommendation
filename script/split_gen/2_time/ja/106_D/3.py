def main():
    N, M, Q = map(int, input().split())
    L = [0] * (M + 1)
    R = [0] * (M + 1)
    for i in range(M):
        L[i + 1], R[i + 1] = map(int, input().split())
    p = [0] * (Q + 1)
    q = [0] * (Q + 1)
    for i in range(Q):
        p[i + 1], q[i + 1] = map(int, input().split())
    ans = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            ans[i][j] = ans[i][j - 1] + ans[i - 1][j] - ans[i - 1][j - 1]
            if L[i] <= j <= R[i]:
                ans[i][j] += 1
    for i in range(1, Q + 1):
        print(ans[q[i]][q[i]] - ans[p[i] - 1][q[i]] - ans[q[i]][p[i] - 1] + ans[p[i] - 1][p[i] - 1])
