def main():
    # 读入数据
    n, m = map(int, input().split())
    # 计算距离
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = ((i + 1) - 1) ** 2 + ((j + 1) - 1) ** 2
    # 计算结果
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= m:
                ans[i][j] = 1
            else:
                ans[i][j] = -1
    # 打印结果
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()