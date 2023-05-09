def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    def get_score(hand):
        if hand == "r":
            return P
        elif hand == "s":
            return R
        elif hand == "p":
            return S
    def get_hand(opp_hand):
        if opp_hand == "r":
            return "p"
        elif opp_hand == "s":
            return "r"
        elif opp_hand == "p":
            return "s"
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][0] = get_score(get_hand(T[0]))
    dp[0][1] = get_score(get_hand(T[0]))
    dp[0][2] = get_score(get_hand(T[0]))
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + get_score(get_hand(T[i]))
        dp[i][1] = dp[i-1][1] + get_score(get_hand(T[i]))
        dp[i][2] = dp[i-1][2] + get_score(get_hand(T[i]))
        if i >= K:
            dp[i][0] = max(dp[i][0], dp[i-K][1] + get_score(get_hand(T[i])))
            dp[i][1] = max(dp[i][1], dp[i-K][2] + get_score(get_hand(T[i])))
            dp[i][2] = max(dp[i][2], dp[i-K][0] + get_score(get_hand(T[i])))
    print(max(dp[N-1]))
main()

if __name__ == '__main__':
    main()