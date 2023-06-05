def main():
    # 读取标准输入
    N, Q = map(int, input().split())
    # print(N, Q)
    # print(type(N), type(Q))
    # 生成一个N*N的二维列表
    matrix = [[0 for i in range(N)] for j in range(N)]
    # print(matrix)
    # print(type(matrix))
    # 读取操作
    for i in range(Q):
        T, A, B = map(int, input().split())
        # print(T, A, B)
        # print(type(T), type(A), type(B))
        if T == 1:
            # A关注B
            matrix[A - 1][B - 1] = 1
        elif T == 2:
            # A取消关注B
            matrix[A - 1][B - 1] = 0
        elif T == 3:
            # 判断A和B是否互相关注
            if matrix[A - 1][B - 1] == 1 and matrix[B - 1][A - 1] == 1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()