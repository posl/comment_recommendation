def main():
    # 读取标准输入
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    # 求解
    ans = 0
    for i in range(2**K):
        dish = [0] * N
        for j in range(K):
            if ((i >> j) & 1):
                dish[C[j] - 1] += 1
            else:
                dish[D[j] - 1] += 1
        cnt = 0
        for j in range(M):
            if dish[A[j] - 1] >= 1 and dish[B[j] - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    # 打印输出
    print(ans)
