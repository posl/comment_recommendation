def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    
    # 1. 预处理
    # 1.1. 从1号房间移动到i号房间的时间
    B = [0] * N
    for i in range(N-1):
        B[i+1] = B[i] + A[i]
    # 1.2. 奖励房间
    R = [0] * N
    for x, y in XY:
        R[x-1] = y
    
    # 2. 動的計画法
    # dp[i] := i号房间的时限
    dp = [0] * N
    dp[0] = T
    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i] - A[i])
        dp[i+1] = min(dp[i+1], T - B[i])
        dp[i+1] += R[i]
    return dp[N-1] >= 0

if __name__ == '__main__':
    solve()