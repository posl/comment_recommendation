def main():
    # 读入数据
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 计算最短距离
    max_len = 0
    for i in range(N):
        if i == N - 1:
            max_len = max(max_len, K - A[i] + A[0])
        else:
            max_len = max(max_len, A[i + 1] - A[i])
    print(K - max_len)

if __name__ == '__main__':
    main()