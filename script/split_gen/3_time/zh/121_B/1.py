def main():
    # 读取数据
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, C)
    # print(B)
    # print(A)
    # 计算结果
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        sum += C
        if sum > 0:
            count += 1
    # 输出结果
    print(count)
