def solve():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    # 用于计算每一分钟的热水总量
    # 0 代表开始，W 代表结束
    imos = [0] * (2 * 10 ** 5 + 2)
    for i in range(N):
        imos[S[i]] += P[i]
        imos[T[i]] -= P[i]
    # 累积和
    for i in range(2 * 10 ** 5 + 1):
        imos[i + 1] += imos[i]
    # 检查是否超过了W
    for i in range(2 * 10 ** 5 + 1):
        if imos[i] > W:
            print("No")
            return
    print("Yes")
