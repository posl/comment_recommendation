def main():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        cards.append(list(map(int, input().split())))
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j - cards[i][0] >= 0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-cards[i][0]]
            if j - cards[i][1] >= 0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-cards[i][1]]
    if dp[N][S]:
        print("Yes")
        ans = []
        for i in range(N-1, -1, -1):
            if S - cards[i][0] >= 0 and dp[i][S-cards[i][0]]:
                ans.append("H")
                S -= cards[i][0]
            else:
                ans.append("T")
                S -= cards[i][1]
        print("".join(ans[::-1]))
    else:
        print("No")

if __name__ == '__main__':
    main()