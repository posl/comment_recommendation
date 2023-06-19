def main():
    # 输入
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 初始化
    max_dis = 0
    for i in range(N - 1):
        dis = A[i + 1] - A[i]
        if dis > max_dis:
            max_dis = dis
    dis = K - A[N - 1] + A[0]
    if dis > max_dis:
        max_dis = dis
    # 输出
    print(K - max_dis)
