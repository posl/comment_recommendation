def main():
    # 读取输入
    N, M = map(int, input().split())
    # 生成一个N*N的矩阵
    matrix = [[0 for i in range(N)] for j in range(N)]
    # 读取人员参加的聚会
    for i in range(M):
        # 读取每个人参加的聚会
        k, *x = map(int, input().split())
        # 生成一个人员参加的聚会的矩阵
        for j in range(k):
            for l in range(j + 1, k):
                matrix[x[j] - 1][x[l] - 1] += 1
                matrix[x[l] - 1][x[j] - 1] += 1
    # 判断是否每两个人都至少参加过一次同一个聚会
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] == 0:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()