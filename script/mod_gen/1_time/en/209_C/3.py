def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    dp = [0 for i in range(N)]
    dp[0] = 1
    for i in range(1, N):
        if C[i] > C[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    ans = 1
    for i in range(N):
        if C[i] > i+1:
            ans = (ans * dp[i]) % mod
        else:
            ans = 0
            break
    print(ans)

if __name__ == '__main__':
    main()