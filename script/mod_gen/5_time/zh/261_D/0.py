def main():
    # 读入输入
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    cy = [list(map(int, input().split())) for _ in range(m)]
    # 初始化
    dp = [0] * (n + 1)
    # dp[0] = 0
    # dp[1] = x[0]
    # dp[2] = x[0] + x[1]
    # dp[3] = x[0] + x[1] + x[2]
    # dp[4] = x[0] + x[1] + x[2] + x[3]
    # ...
    # dp[n] = x[0] + x[1] + ... + x[n-1]
    for i in range(n):
        dp[i+1] = dp[i] + x[i]
    # 算法
    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            # i < j
            # c_i < c_j
            # y_i < y

if __name__ == '__main__':
    main()