def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0]*10
    for i in range(10):
        dp = [0]*N
        if i == A[0]:
            dp[0] = 1
        for j in range(1, N):
            if i == A[j]:
                dp[j] = (dp[j-1]*2 + 1) % MOD
            else:
                dp[j] = dp[j-1]
        ans[i] = dp[-1]
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()