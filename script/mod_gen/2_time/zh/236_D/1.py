def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # print(A)
    # print(len(A))
    # 暴力解法
    # max = 0
    # for i in range(len(A)):
    #     for j in range(i+1, len(A)):
    #         if max < A[i][j]:
    #             max = A[i][j]
    # print(max)
    # 位运算
    # max = 0
    # for i in range(len(A)):
    #     for j in range(i+1, len(A)):
    #         if max < A[i][j]:
    #             max = A[i][j]
    # print(max)
    # 位运算
    max = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if max < A[i][j]:
                max = A[i][j]
    print(max)

if __name__ == '__main__':
    main()