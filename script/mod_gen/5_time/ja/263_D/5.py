def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] -= R
    #print(A)
    dp = [[0,0] for _ in range(N+1)]
    for i in range(N):
        dp[i+1][0] = min(dp[i][0], dp[i][1])
        dp[i+1][1] = min(dp[i][0], dp[i][1]) + A[i]
    #print(dp)
    print(min(dp[N][0], dp[N][1]) + L * N)
main()

if __name__ == '__main__':
    main()