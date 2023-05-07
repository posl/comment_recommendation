def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        if dp[i] == -1:
            continue
        for j in a:
            if i+j > n:
                continue
            dp[i+j] = max(dp[i+j], dp[i]+1)
    ans = ''
    i = n
    while i > 0:
        for j in a:
            if i-j < 0:
                continue
            if dp[i-j] == dp[i]-1:
                ans += str(j)
                i -= j
                break
    print(ans)

if __name__ == '__main__':
    main()