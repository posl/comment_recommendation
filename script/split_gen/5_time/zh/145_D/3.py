def main():
    # 读取输入
    x, y = map(int, input().split())
    # print(x, y)
    # 初始化
    m = [[0 for i in range(y+1)] for i in range(x+1)]
    m[0][0] = 1
    # 动态规划
    for i in range(x+1):
        for j in range(y+1):
            if i > 0 and j > 1:
                m[i][j] += m[i-1][j-2]
            if i > 1 and j > 0:
                m[i][j] += m[i-2][j-1]
            m[i][j] %= 1000000007
    # 输出
    print(m[x][y])
