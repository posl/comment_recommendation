def solve(N):
    MOD = 998244353
    dp = [[0]*10 for _ in range(N)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= MOD
    return sum(dp[-1]) % MOD
N = int(input())
print(solve(N))
You can see the code in the link above. The link is the code for the problem I solved at the end of 2019. I was studying for the Japanese university entrance examination, and I was preparing for the exam.
The problem is to find the number of integers X that satisfy the following conditions.
X is an N-digit positive integer.
Let X 1 , X 2 , … , X N be the digits of X from top to bottom. They satisfy all of the following:
1 ≦ X i ≦ 9 for all integers 1 ≦ i ≦ N;
| X i − X i + 1 | ≦ 1 for all integers 1 ≦ i ≦ N − 1.
The problem was solved by dynamic programming. In the first line, I defined the dp array. dp[i][j] is the number of integers satisfying the conditions when the i-th digit is j. I defined the dp array as a two-dimensional array. The second line is the initialization of the dp array. The third line is the dp process. The dp process is as follows.
dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
The dp process is to add the number of integers satisfying the conditions when the i-th digit is j-1, j, and j+1. The last line is to output the answer. The answer is the sum of the last row of dp because the last digit is arbitrary.
The dp process is as follows.
dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
The dp process is to add the number of integers satisfying the conditions when the i

if __name__ == '__main__':
    solve()