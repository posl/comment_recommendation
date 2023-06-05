def main():
    # 读取输入
    n, k = map(int, input().split())
    # 生成组合数表
    comb = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        comb[i][0] = 1
        for j in range(1, k + 1):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % (10 ** 9 + 7)
    # 计算答案
    ans = [0 for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                ans[i] = (ans[i] + comb[n - (i - 1) * j][j]) % (10 ** 9 + 7)
    # 输出
    for i in range(1, k + 1):
        print(ans[i])
