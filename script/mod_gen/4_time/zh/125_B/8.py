def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    #dp[i][j]表示前i个宝石中，总价值为j时的最小费用
    dp = [[float('inf') for _ in range(10000)] for _ in range(10000)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(10000):
            if j < V[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j - V[i]] + C[i])
    print(max([i for i in range(10000) if dp[N][i] <= i]))

if __name__ == '__main__':
    main()