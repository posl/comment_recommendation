def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    #dp[i][j] i枚目まで見たときにjの合計ができるか
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j] == 1:
                if a[i] + j <= S:
                    dp[i + 1][a[i] + j] = 1
                if b[i] + j <= S:
                    dp[i + 1][b[i] + j] = 1
    if dp[N][S] == 1:
        print("Yes")
        ans = ""
        for i in range(N):
            if dp[N - i - 1][S - a[N - i - 1]] == 1:
                ans += "H"
                S -= a[N - i - 1]
            else:
                ans += "T"
                S -= b[N - i - 1]
        print(ans[::-1])
    else:
        print("No")

if __name__ == '__main__':
    main()