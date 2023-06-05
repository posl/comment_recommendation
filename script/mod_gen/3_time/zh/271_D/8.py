def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = 1
                if j + a[i] <= s:
                    dp[i+1][j+a[i]] = 1
                if j + b[i] <= s:
                    dp[i+1][j+b[i]] = 1
    if not dp[n][s]:
        print("No")
        return
    print("Yes")
    ans = ""
    for i in range(n-1, -1, -1):
        if s - a[i] >= 0 and dp[i][s-a[i]]:
            ans += "H"
            s -= a[i]
        else:
            ans += "T"
            s -= b[i]
    print(ans[::-1])

if __name__ == '__main__':
    main()