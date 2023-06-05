def main():
    # 读取输入
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    # 为列车的左端点和右端点分别建立累计和
    L = [0] * (N + 2)
    R = [0] * (N + 2)
    for l, r in LR:
        L[l] += 1
        R[r + 1] -= 1
    for i in range(1, N + 2):
        L[i] += L[i - 1]
        R[i] += R[i - 1]
    # 计算累计和的差，即为答案
    for p, q in PQ:
        print(L[q] - L[p - 1] - R[q])

if __name__ == '__main__':
    main()