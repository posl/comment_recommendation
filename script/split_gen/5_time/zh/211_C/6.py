def main():
    # 读入数据
    S = input()
    # 生成目标字符串
    target = "chokudai"
    # 生成dp数组
    dp = [[0 for i in range(len(S))] for j in range(len(target))]
    # 计算dp数组
    for i in range(len(S)):
        for j in range(len(target)):
            if i == 0 and j == 0:
                if S[i] == target[j]:
                    dp[j][i] = 1
            elif i == 0:
                dp[j][i] = 0
            elif j == 0:
                dp[j][i] = dp[j][i - 1]
                if S[i] == target[j]:
                    dp[j][i] += 1
            else:
                dp[j][i] = dp[j][i - 1]
                if S[i] == target[j]:
                    dp[j][i] += dp[j - 1][i - 1]
    # 输出结果
    print(dp[len(target) - 1][len(S) - 1] % (10 ** 9 + 7))
