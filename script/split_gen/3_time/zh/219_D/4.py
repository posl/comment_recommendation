def main():
    # 读入数据
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # 递推
    dp = [[False for j in range(y + 1)] for i in range(x + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j - a[i] >= 0 and k - b[i] >= 0:
                    dp[j][k] |= dp[j - a[i]][k - b[i]]
    # 输出结果
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)
