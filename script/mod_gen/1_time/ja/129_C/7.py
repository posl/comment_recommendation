def main():
    N, M = [int(i) for i in input().split()]
    A = [int(input()) for i in range(M)]
    A.append(0)
    A.append(N+1)
    A.sort()
    A = [A[i+1]-A[i]-1 for i in range(M+1)]
    dp = [0]*(M+2)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, M+2):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    ans = 1
    for i in range(M+1):
        ans *= dp[A[i]]
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()