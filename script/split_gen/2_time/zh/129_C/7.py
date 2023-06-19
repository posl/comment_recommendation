def main():
    # 读取输入
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    # 从第0阶开始爬楼梯
    dp = [0] * (n + 1)
    dp[0] = 1
    # 爬楼梯
    for i in range(1, n + 1):
        if i not in a:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    # 打印结果
    print(dp[n])
