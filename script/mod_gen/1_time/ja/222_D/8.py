def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[i][j] = (a1, a2, ..., ai) であって、ai = j であるようなものの個数
    dp = [[0] * 3001 for _ in range(3001)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            for k in range(j + 1):
                dp[i + 1][j] += dp[i][k]
                dp[i + 1][j] %= 998244353
    ans = 0
    for i in range(3001):
        ans += dp[N][i]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()