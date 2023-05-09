def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [0 for _ in range(3001)]
    dp[0] = 1
    for i in range(N):
        tmp = [0 for _ in range(3001)]
        for j in range(A[i], B[i]+1):
            tmp[j] = dp[j]
        for j in range(1, 3001):
            tmp[j] += tmp[j-1]
            tmp[j] %= MOD
        dp = tmp
    print(dp[3000])
main()
