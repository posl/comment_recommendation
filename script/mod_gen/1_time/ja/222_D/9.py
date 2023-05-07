def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # dp[i][j] = b[i]まで見た時に、a[i]以上b[i]以下の数列の個数
    dp = [[0 for _ in range(3001)] for _ in range(n)]
    for i in range(a[0], b[0]+1):
        dp[0][i] = 1
    
    for i in range(1, n):
        # 累積和
        for j in range(1, 3001):
            dp[i][j] = (dp[i][j] + dp[i][j-1]) % 998244353
        
        # a[i]以上b[i]以下の数列の個数
        for j in range(a[i], b[i]+1):
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % 998244353
    
    print(dp[n-1][b[n-1]])

if __name__ == '__main__':
    main()