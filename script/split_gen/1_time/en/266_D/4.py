def main():
    N = int(input())
    A = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        A.append([T, X, A])
    A.sort()
    dp = [[0] * 5 for _ in range(N)]
    for i in range(N):
        for j in range(5):
            if A[i][1] == j:
                dp[i][j] = A[i][2]
    for i in range(1, N):
        for j in range(5):
            if A[i][0] == A[i - 1][0]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][A[i][1]] + A[i][2])
    print(max(dp[N - 1]))
