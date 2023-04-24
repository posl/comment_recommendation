Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    mod = 998244353
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    n = 2
    a = [1, 1]
    b = [2, 3]
    c = []
    for i in range(n):
        c.append([a[i], b[i]])
    print(c)
    print("n = ", n)
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("answer = ", answer(n, c))
    return

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3001):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
            if A[i] <= j <= B[i]:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
    print(dp[N][3000])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1)
    print(ans%998244353)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(b[i], n) - a[i] + 1
    print(ans % 998244353)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    C = [0] * N
    for i in range(N):
        C[i] = B[i] - A[i] + 1
    ans = 1
    for i in range(N):
        ans *= C[i]
        ans %= mod
    print(ans)

=======
Suggestion 7

def solve():
    # 標準入力から入力値を取得する
    N = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    # 初期処理
    MOD = 998244353
    # 処理
    # dp[i][j] = (i番目までの数列で、j番目の要素までを決めたときの場合の数)
    dp = [[0 for j in range(max(b_list)+1)] for i in range(N)]
    for j in range(a_list[0], b_list[0]+1):
        dp[0][j] = 1
    for i in range(1, N):
        for j in range(a_list[i], b_list[i]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    # 出力
    print(sum(dp[N-1]) % MOD)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # dp[i][j] は i 番目まで決めたとき、j 以下の値を持つ数列の個数
    dp = [[0] * 3001 for _ in range(N + 1)]

    dp[0][0] = 1
    for i in range(1, N + 1):
        # 累積和
        for j in range(1, 3001):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 998244353

        # 範囲を絞る
        for j in range(A[i - 1], B[i - 1] + 1):
            dp[i][j] = dp[i - 1][j]

    print(dp[N][3000])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[i][j] = (a1, a2, ..., ai) であって、ai = j であるようなものの個数
    dp = [[0] * 3001 for _ in range(3001)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            for k in range(j + 1):
                dp[i + 1][j] += dp[i][k]
                dp[i + 1][j] %= 998244353
    ans = 0
    for i in range(3001):
        ans += dp[N][i]
        ans %= 998244353
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # dp[i][j] = b[i]まで見た時に、a[i]以上b[i]以下の数列の個数
    dp = [[0 for _ in range(3001)] for _ in range(n)]
    for i in range(a[0], b[0]+1):
        dp[0][i] = 1
    
    for i in range(1, n):
        # 累積和
        for j in range(1, 3001):
            dp[i][j] = (dp[i][j] + dp[i][j-1]) % 998244353
        
        # a[i]以上b[i]以下の数列の個数
        for j in range(a[i], b[i]+1):
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % 998244353
    
    print(dp[n-1][b[n-1]])
