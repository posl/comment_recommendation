def solve():
    # N:卡片数目，S:目标和
    N, S = map(int, input().split())
    # a:正面数字，b:背面数字
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    # 使用动态规划
    # dp[i][j]:表示前i张牌中，能否组成和j
    # dp[i][j] = dp[i-1][j-a[i]] or dp[i-1][j-b[i]]
    dp = [[False] * (S+1) for i in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j >= a[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-a[i]]
            if j >= b[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-b[i]]
    if dp[N][S]:
        print("Yes")
        # 从后往前推，找出是哪张牌的正面或者背面
        ans = ""
        for i in range(N-1, -1, -1):
            if S >= a[i] and dp[i][S-a[i]]:
                ans += "H"
                S -= a[i]
            else:
                ans += "T"
                S -= b[i]
        print(ans[::-1])
    else:
        print("No")

if __name__ == '__main__':
    solve()