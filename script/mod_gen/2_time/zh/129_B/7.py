def solve():
    N = int(input())
    W = list(map(int, input().split()))
    # 从 1 到 N-1 之间的所有整数 T，计算 S_1 和 S_2 的绝对差值的最小值
    ans = 1000000000
    for t in range(1, N):
        # S_1 和 S_2 的初始值设为 0
        s1 = 0
        s2 = 0
        # 在索引 i = 0 到 i = T-1 之间的所有整数 i，将 W_i 加到 S_1
        for i in range(t):
            s1 += W[i]
        # 在索引 i = T 到 i = N-1 之间的所有整数 i，将 W_i 加到 S_2
        for i in range(t, N):
            s2 += W[i]
        # 更新答案
        ans = min(ans, abs(s1 - s2))
    print(ans)
solve()
