def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                if j + a[i] <= S:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= S:
                    dp[i + 1][j + b[i]] = True
    if dp[N][S]:
        print("Yes")
        ans = []
        i = N
        j = S
        while i > 0:
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans.append("H")
                j -= a[i - 1]
            else:
                ans.append("T")
                j -= b[i - 1]
            i -= 1
        ans.reverse()
        print("".join(ans))
    else:
        print("No")

if __name__ == '__main__':
    main()