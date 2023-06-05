def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    #C = (c_1, c_2, ..., c_N)
    #a_i ≦ c_i ≦ b_i，对于每一个i（1 ≦ i ≦ N）。
    #找出能成为C的序列的数量，模数为998244353。
    #dp[i][j] = (a_i ≦ c_i ≦ j)的数量
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = 1
    for i in range(N):
        for j in range(1, 3001):
            if i == 0:
                dp[i][j] += dp[i][j-1]
            else:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= MOD
    print(dp[N-1][3000])
    return
main()
