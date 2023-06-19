def main():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    # dp[i][j] = True if j is reachable using cards[0:i]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        a, b = cards[i]
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a <= S:
                    dp[i + 1][j + a] = True
                if j + b <= S:
                    dp[i + 1][j + b] = True
    if dp[N][S]:
        print("Yes")
        ans = ["H"] * N
        for i in range(N - 1, 0, -1):
            a, b = cards[i]
            if S - a >= 0 and dp[i][S - a]:
                ans[i] = "T"
                S -= a
            else:
                ans[i] = "H"
                S -= b
        ans[0] = "H" if S - cards[0][0] >= 0 else "T"
        print("".join(ans))
    else:
        print("No")
