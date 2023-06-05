def main():
    # 读入数据
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算最大距离
    max_dist = 0
    for i in range(N):
        if i == N - 1:
            dist = K - A[i] + A[0]
        else:
            dist = A[i + 1] - A[i]
        if dist > max_dist:
            max_dist = dist
    # 计算答案
    print(K - max_dist)
main()
