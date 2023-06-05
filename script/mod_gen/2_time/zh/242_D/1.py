def main():
    from sys import stdin
    import numpy as np
    from numba import njit
    @njit
    def solve(N):
        dp = np.zeros((N+1, 9), dtype=np.int64)
        dp[1] = 1
        for i in range(2, N+1):
            for j in range(9):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
                elif j == 8:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        return sum(dp[N]) % 998244353
    N = int(stdin.readline().rstrip())
    print(solve(N))

if __name__ == '__main__':
    main()