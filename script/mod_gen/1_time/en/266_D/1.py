def main():
    N = int(input())
    X = [0]*N
    A = [0]*N
    T = [0]*N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0]*5 for _ in range(N+1)]
    for i in range(N):
        for j in range(5):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if T[i] >= abs(j-X[i]):
                dp[i+1][X[i]] = max(dp[i+1][X[i]], dp[i][j]+A[i])
    print(max(dp[N]))

if __name__ == '__main__':
    main()