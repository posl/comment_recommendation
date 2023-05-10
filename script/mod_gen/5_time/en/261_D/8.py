def resolve():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    #s = input().rstrip().decode()
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = [list(map(int, input().split())) for i in range(m)]
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    #c = list(map(int, input().split()))
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
            for k in range(m):
                if i + 1 == y[k][0]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + y[k][1])
            if i + 1 + j + 1 <= n:
                dp[i + 1 + j + 1][0] = max(dp[i + 1 + j + 1][0], dp[i][j] + sum(x[i + 1:i + 1 + j + 1]))
    print(max(dp[n]))

if __name__ == '__main__':
    resolve()