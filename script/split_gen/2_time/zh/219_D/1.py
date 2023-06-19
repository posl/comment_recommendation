def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][min(j + A[i], X)][min(k + B[i], Y)] |= dp[i][j][k]
                dp[i + 1][j][k] |= dp[i][j][k]
    ans = -1
    for i in range(1, N + 1):
        if dp[i][X][Y]:
            ans = i
            break
    print(ans)
