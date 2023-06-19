def main():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    # print(N, S, cards)
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j >= cards[i][0]:
                dp[i+1][j] |= dp[i][j-cards[i][0]]
            if j >= cards[i][1]:
                dp[i+1][j] |= dp[i][j-cards[i][1]]
    if dp[N][S]:
        print("Yes")
        ans = ""
        i, j = N, S
        while i > 0 and j > 0:
            if j >= cards[i-1][0] and dp[i-1][j-cards[i-1][0]]:
                ans += "H"
                j -= cards[i-1][0]
            else:
                ans += "T"
                j -= cards[i-1][1]
            i -= 1
        print(ans[::-1])
    else:
        print("No")

if __name__ == '__main__':
    main()