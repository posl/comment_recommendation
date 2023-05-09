def main():
    n, s = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    # dp[i][j] = 1 if it is possible to make sum j using the first i cards
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                if j + a[i] <= s:
                    dp[i + 1][j + a[i]] = 1
                if j + b[i] <= s:
                    dp[i + 1][j + b[i]] = 1
    if dp[n][s] == 0:
        print("No")
        return
    print("Yes")
    ans = ["H"] * n
    i = n
    j = s
    while i > 0 and j > 0:
        if j >= a[i - 1] and dp[i - 1][j - a[i - 1]]:
            ans[i - 1] = "H"
            j -= a[i - 1]
        else:
            ans[i - 1] = "T"
            j -= b[i - 1]
        i -= 1
    print("".join(ans))

if __name__ == '__main__':
    main()