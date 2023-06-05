def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                if j + a[i] <= s:
                    dp[i+1][j+a[i]] = True
                if j + b[i] <= s:
                    dp[i+1][j+b[i]] = True
    if dp[n][s]:
        print("Yes")
        ans = ""
        i = n
        j = s
        while i > 0:
            if j-a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans = "H" + ans
                j -= a[i-1]
            else:
                ans = "T" + ans
                j -= b[i-1]
            i -= 1
        print(ans)
    else:
        print("No")

if __name__ == '__main__':
    main()