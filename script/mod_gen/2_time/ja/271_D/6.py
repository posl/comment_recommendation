def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[False] * (S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j < a[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = dp[i][j] or dp[i][j-a[i]]
            if j < b[i]:
                dp[i+1][j] = dp[i+1][j]
            else:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-b[i]]
    if dp[N][S]:
        print('Yes')
        ans = []
        i = N
        j = S
        while i > 0:
            if j < a[i-1]:
                ans.append('T')
                i -= 1
            elif dp[i-1][j-a[i-1]]:
                ans.append('H')
                j -= a[i-1]
                i -= 1
            else:
                ans.append('T')
                i -= 1
        print(''.join(ans[::-1]))
    else:
        print('No')

if __name__ == '__main__':
    main()