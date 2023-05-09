def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(tuple(map(int, input().split())))
    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a, b = cards[i]
        for j in range(S+1):
            if dp[i][j]:
                dp[i+1][j] = 1
                if j+a <= S:
                    dp[i+1][j+a] = 1
                if j+b <= S:
                    dp[i+1][j+b] = 1
    if dp[N][S]:
        ans = ""
        for i in range(N-1, -1, -1):
            a, b = cards[i]
            if S-a >= 0 and dp[i][S-a]:
                ans += "T"
                S -= a
            else:
                ans += "H"
                S -= b
        print("Yes")
        print(ans[::-1])
    else:
        print("No")
