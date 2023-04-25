Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if k + j <= K:
                    dp[i + 1][k + j] += dp[i][j]
                    dp[i + 1][k + j] %= MOD
    print(dp[-1][-1])

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j] * M % mod
            if j >= i:
                dp[i][j] = (dp[i][j] + dp[i][j - i]) % mod
    print(dp[N][K])

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD
    print(dp[N][K])

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD
    print(dp[N][K])

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            for k in range(i, K + 1):
                dp[i][k] += dp[i - 1][k - j]
                dp[i][k] %= mod
    print(dp[N][K])

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    mod = 998244353

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod

    ans = 0
    for i in range(K+1):
        ans += dp[N][i]
        ans %= mod

    print(ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[[0] * (K + 1) for i in range(M + 1)] for j in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M + 1):
            for k in range(K + 1):
                for l in range(j + 1):
                    if k + l <= K:
                        dp[i + 1][j][k + l] += dp[i][j - l][k]
                        dp[i + 1][j][k + l] %= mod
    print(sum(dp[N][M]) % mod)

=======
Suggestion 8

def solve():
    N, M, K = map(int, input().split())

    mod = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    dp[i + 1][j + k] += dp[i][j]
                    dp[i + 1][j + k] %= mod
    print(dp[N][K])

=======
Suggestion 9

def   main (): 
     N ,   M ,   K   =   map ( int ,   input (). split ()) 
     MOD   =   998244353 

     dp   =   [ [ 0 ]   *   ( K   +   1 )   for   _   in   range ( N   +   1 )] 
     dp [ 0 ][ 0 ]   =   1 
     for   i   in   range ( N ): 
         for   j   in   range ( K   +   1 ): 
             for   k   in   range ( M   +   1 ): 
                 if   j   +   k   >   K : 
                     break 
                 dp [ i   +   1 ][ j   +   k ]   +=   dp [ i ][ j ] 
                 dp [ i   +   1 ][ j   +   k ]   %=   MOD 
     print ( dp [ N ][ K ])

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, M + 1):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(1, K + 1):
            for k in range(1, M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= MOD
    print(dp[-1][-1])
