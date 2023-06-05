def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    # print(N, A)
    # 计算直属下级的数量
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    # print(B)
    # 输出结果
    for i in range(N):
        print(B[i])

if __name__ == '__main__':
    main()