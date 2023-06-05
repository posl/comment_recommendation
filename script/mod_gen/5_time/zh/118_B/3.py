def main():
    # N M
    N, M = map(int, input().split())
    # K_1 A_{11}A_{12}...A_{1K_1}
    # K_2 A_{21}A_{22} ...A_{2K_2}
    # :
    # K_N A_{N1}A_{N2} ...A_{NK_N}
    # 用二维数组表示
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # 用一个数组表示食物的被喜爱的次数
    # 初始化为0
    food = [0] * M
    # 遍历A数组
    for i in range(N):
        # 遍历A[i]数组，注意下标从1开始
        for j in range(1, A[i][0] + 1):
            food[A[i][j] - 1] += 1
    # 统计food数组中值为N的个数
    count = 0
    for i in range(M):
        if food[i] == N:
            count += 1
    print(count)

if __name__ == '__main__':
    main()