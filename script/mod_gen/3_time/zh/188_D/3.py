def main():
    # 读入数据
    N, C = map(int, input().split())
    # 服务开始时间
    A = []
    # 服务结束时间
    B = []
    # 服务费用
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # 找到最晚结束的服务
    maxB = max(B)
    # 计算每日费用
    dailyFee = [0] * (maxB + 1)
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dailyFee[j] += C[i]
    # 计算最小费用
    minFee = sum(C)
    for i in range(1, maxB + 1):
        if dailyFee[i] < minFee:
            minFee = dailyFee[i]
    print(minFee)

if __name__ == '__main__':
    main()