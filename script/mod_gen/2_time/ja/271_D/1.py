def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    # dp[i][j] := i 枚目までのカードからなる部分集合で、表になっているカードの面の和が j になるようにカードを置くことができるか
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a[i] <= S:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= S:
                    dp[i + 1][j + b[i]] = True
    if dp[N][S]:
        print('Yes')
        ans = ''
        j = S
        for i in range(N, 0, -1):
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans += 'H'
                j -= a[i - 1]
            else:
                ans += 'T'
                j -= b[i - 1]
        print(ans[::-1])
    else:
        print('No')

if __name__ == '__main__':
    main()