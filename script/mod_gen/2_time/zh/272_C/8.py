def main():
    # 读取输入
    N, M = map(int, input().split())
    # 生成一个N*N的矩阵
    matrix = [[0] * N for i in range(N)]
    # 读取每一行的数据
    for i in range(M):
        # 读取每一行的数据
        row = list(map(int, input().split()))
        # 读取每一行的第一个数据，即人数
        k = row[0]
        # 读取每一行的后面数据，即每个人的编号
        # 两个人参加了同一个聚会，即两个人的编号在矩阵中对应的位置的值为1
        for j in range(1, k + 1):
            for l in range(j + 1, k + 1):
                matrix[row[j] - 1][row[l] - 1] = matrix[row[l] - 1][row[j] - 1] = 1
    # 判断矩阵中是否有0，如果有0，则说明有两个人没有参加同一个聚会
    # 如果没有0，则说明每两个人都参加了同一个聚会
    if 0 in matrix:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()