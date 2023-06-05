def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    # print(N, X)
    # print(A)
    # print(B)
    # 第i个阶段清除一次的时间
    # T1 = [A[i] + B[i] for i in range(N)]
    # print(T1)
    # 第i个阶段清除X次的时间
    T = [A[i] * X + B[i] for i in range(N)]
    # print(T)
    # 第i个阶段清除X次的时间的前缀和
    T_sum = [0] * N
    T_sum[0] = T[0]
    for i in range(1, N):
        T_sum[i] = T_sum[i - 1] + T[i]
    # print(T_sum)
    # 第i个阶段清除X次的时间的后缀和
    T_sum_r = [0] * N
    T_sum_r[N - 1] = T[N - 1]
    for i in range(N - 2, -1, -1):
        T_sum_r[i] = T_sum_r[i + 1] + T[i]
    # print(T_sum_r)
    ans = 0
    for i in range(N):
        if i == 0:
            ans = T_sum_r[i + 1] + (N - 1) * T[i]
        elif i == N - 1:
            ans = T_sum[i - 1] + (N - 1) * T[i]
        else:
            ans = min(ans, T_sum[i - 1] + T_sum_r[i + 1] + (N - 1) * T[i])
    print(ans)
solve()
