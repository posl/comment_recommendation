def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # dp[i][j] := i枚目まで見たときに、jを作ることができるかどうか
    dp = [[False for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = True
    for i in range(1, N+1):
        for j in range(S+1):
            if dp[i-1][j]:
                dp[i][j] = True
                if j+a[i-1] <= S:
                    dp[i][j+a[i-1]] = True
                if j+b[i-1] <= S:
                    dp[i][j+b[i-1]] = True
    if dp[N][S]:
        print('Yes')
        ans = ''
        j = S
        for i in range(N, 0, -1):
            if j-a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans += 'H'
                j -= a[i-1]
            else:
                ans += 'T'
                j -= b[i-1]
        print(ans[::-1])
    else:
        print('No')

if __name__ == '__main__':
    main()