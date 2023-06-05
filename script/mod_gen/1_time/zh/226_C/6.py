def main():
    # 读入数据
    # N = 3
    # T = [3, 5, 7]
    # K = [0, 1, 1]
    # A = [[], [1], [1]]
    # N = 5
    # T = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    # K = [0, 0, 0, 0, 4]
    # A = [[], [], [], [], [1, 2, 3, 4]]
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        T_i, K_i, *A_i = map(int, input().split())
        T.append(T_i)
        K.append(K_i)
        A.append(A_i)
    # print(N, T, K, A)
    # 从后往前遍历
    # dp[i]: 学习第i步所需的最少时间
    # dp[i] = max(dp[A[i][j]] + T[A[i][j]] for j in range(K[i]))
    # print(A)
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        if K[i] == 0:
            dp[i] = T[i]
        else:
            dp[i] = max(dp[A[i][j]] + T[A[i][j]] for j in range(K[i]))
    print(max(dp))

if __name__ == '__main__':
    main()