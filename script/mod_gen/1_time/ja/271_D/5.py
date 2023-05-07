def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # dp[i][j]: i枚目までのカードを使ってjを作ることができるかどうか
    dp = [[False for i in range(S+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j-a[i] >= 0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            if j-b[i] >= 0 and dp[i][j-b[i]]:
                dp[i+1][j] = True
    if dp[N][S]:
        print("Yes")
        ans = ""
        for i in range(N-1, -1, -1):
            if S-a[i] >= 0 and dp[i][S-a[i]]:
                ans += "H"
                S -= a[i]
            else:
                ans += "T"
                S -= b[i]
        print(ans[::-1])
    else:
        print("No")

if __name__ == '__main__':
    main()