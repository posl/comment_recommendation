def solve(card, S):
    # 将第i张牌的正面可见，第j张牌的背面可见，第k张牌的背面可见
    dp = [[[False for _ in range(S+1)] for _ in range(S+1)] for _ in range(len(card)+1)]
    dp[0][0][0] = True
    for i in range(len(card)):
        for j in range(S+1):
            for k in range(S+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j+card[i][0] <= S:
                        dp[i+1][j+card[i][0]][k] = True
                    if k+card[i][1] <= S:
                        dp[i+1][j][k+card[i][1]] = True
    if not dp[len(card)][S][S]:
        return False, []
    else:
        ans = []
        i = len(card)
        j = S
        k = S
        while i > 0:
            if dp[i-1][j][k]:
                ans.append('H')
            elif j-card[i-1][0] >= 0 and dp[i-1][j-card[i-1][0]][k]:
                ans.append('T')
                j -= card[i-1][0]
            else:
                ans.append('F')
                k -= card[i-1][1]
            i -= 1
        return True, ans[::-1]
