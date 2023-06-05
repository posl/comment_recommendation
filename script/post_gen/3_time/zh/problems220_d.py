Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * 10 for _ in range(n)]
    dp[0][a[0]] = 1
    for i in range(1, n):
        for j in range(10):
            dp[i][(j + a[i]) % 10] += dp[i - 1][j]
            dp[i][(j + a[i]) % 10] %= mod
            dp[i][(j * a[i]) % 10] += dp[i - 1][j]
            dp[i][(j * a[i]) % 10] %= mod
    for i in range(10):
        print(dp[n - 1][i])

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = 998244353
    ans = [0] * 10
    ans[a[0]] = 1
    for i in range(1, n):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + a[i]) % 10] += ans[j]
            tmp[(j + a[i]) % 10] %= m
            tmp[(j * a[i]) % 10] += ans[j]
            tmp[(j * a[i]) % 10] %= m
        ans = tmp
    for i in range(10):
        print(ans[i])


solve()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 2**N通りの操作の結果を求める
    # dp[i][j] := i番目までの数字を使って、最後の数字をjにする方法の数
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][A[0]] = 1
    for i in range(N - 1):
        for j in range(10):
            dp[i + 1][(j + A[i + 1]) % 10] += dp[i][j]
            dp[i + 1][(j + A[i + 1]) % 10] %= 998244353
            dp[i + 1][(j * A[i + 1]) % 10] += dp[i][j]
            dp[i + 1][(j * A[i + 1]) % 10] %= 998244353

    # 出力
    for i in range(10):
        print(dp[N - 1][i])

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    # N = 3
    # A = [2,7,6]
    ans = [0]*10
    for i in range(10):
        if i == A[-1]:
            ans[i] = 1
    for i in range(N-2,-1,-1):
        new = [0]*10
        for j in range(10):
            if (j+A[i])%10 == A[i+1]:
                new[j] += ans[j]
            if (j*A[i])%10 == A[i+1]:
                new[j] += ans[j]
        ans = new
    for i in range(10):
        print(ans[i])

solve()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(N)]
        for j in range(10):
            if i == A[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        for j in range(1, N):
            for k in range(10):
                if k == A[j]:
                    dp[j][k] = sum(dp[j - 1]) % mod
                else:
                    dp[j][k] = dp[j - 1][k]
        ans[i] = sum(dp[-1]) % mod
    print('\n'.join(map(str, ans)))

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10

    def f(x, y):
        return (x + y) % 10

    def g(x, y):
        return (x * y) % 10

    for i in range(10):
        for j in range(10):
            for k in range(10):
                dp = [0] * 10
                dp[f(f(i, j), k)] = 1
                dp[f(g(i, j), k)] = 1
                dp[g(f(i, j), k)] = 1
                dp[g(g(i, j), k)] = 1
                for a in range(10):
                    ans[a] += dp[a] * A.count(i) * A.count(j) * A.count(k)
                    ans[a] %= MOD
    for i in range(10):
        print(ans[i])

solve()

=======
Suggestion 8

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    ans = [0] * 10
    for i in range(n):
        ans[A[i]] += 1
    for i in range(10):
        print(ans[i])

=======
Suggestion 9

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    if n == 1:
        print(1)
        return
    if n == 2:
        if (a[0] + a[1]) % 10 == 0:
            print(1)
        else:
            print(0)
        return
    # 从左到右，每次删除两个数，只能是操作F或操作G
    # 操作F：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x+y）%10。
    # 操作G：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x×y）%10。
    # 从左到右，每次删除两个数，只能是操作F或操作G
    # 操作F：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x+y）%10。
    # 操作G：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x×y）%10。
    # 操作F：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x+y）%10。
    # 操作G：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x×y）%10。
    # 操作F：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x+y）%10。
    # 操作G：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x×y）%10。
    # 操作F：删除最左边的两个值（我们称它们为x和y），然后在左端插入（x+y）%10。
