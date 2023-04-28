Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for a in A:
        ans[a] += 1
    for i in range(10):
        for j in range(10):
            ans[(i+j)%10] += ans[i] * ans[j]
    for i in range(10):
        print(ans[i]%MOD)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N):
            if A[j] == i:
                ans[i] += 1
    for i in range(10):
        for j in range(1, N):
            ans[i] = ans[i] * (N - j) % MOD
    for i in range(10):
        print(ans[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N):
            if A[j] == i:
                ans[i] += 1
    for i in range(10):
        ans[i] %= MOD
    for i in range(10):
        for j in range(10):
            if i + j < 10:
                ans[i + j] += ans[i] * ans[j]
                ans[i + j] %= MOD
            else:
                ans[i + j - 10] += ans[i] * ans[j]
                ans[i + j - 10] %= MOD
    for i in range(10):
        print(ans[i])

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        nans = [0] * 10
        for j in range(10):
            nans[(j + A[i]) % 10] += ans[j]
            nans[(j * A[i]) % 10] += ans[j]
        ans = [x % mod for x in nans]
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N):
            if A[j] == i:
                ans[i] += 1
    for i in range(1, N):
        ans2 = [0] * 10
        for j in range(10):
            for k in range(10):
                ans2[(j + k) % 10] += ans[j] * ans[k]
                ans2[(j * k) % 10] += ans[j] * ans[k]
        ans = ans2
    for i in range(10):
        print(ans[i] % mod)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for a in A:
        ans[a] += 1
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        if (i + j * k + l * m) % 10 == A[-1]:
                            ans[i] = (ans[i] + ans[j] * ans[k] * ans[l] * ans[m]) % mod
    for i in range(10):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * 10
    count[A[-1]] = 1
    for i in range(N - 1):
        c = [0] * 10
        for j in range(10):
            c[(j + A[-i - 2]) % 10] += count[j]
            c[(j * A[-i - 2]) % 10] += count[j]
        count = c
    for i in range(10):
        print(count[i] % 998244353)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(N):
            next = [0] * 10
            for k in range(10):
                next[(k + A[j]) % 10] += dp[k]
                next[(k * A[j]) % 10] += dp[k]
            dp = next
        ans[i] = dp[0]
    print("\n".join(map(str, ans)))

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)

    for i in range(n-1):
        new_ans = [0] * 10
        for j in range(10):
            for k in range(10):
                new_ans[(j+k)%10] += ans[j] * ans[k]
                new_ans[(j*k)%10] += ans[j] * ans[k]
        ans = new_ans

    for i in range(10):
        print(ans[i] % 998244353)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353

    ans = [0 for i in range(10)]

    for i in range(10):
        for j in range(10):
            for k in range(10):
                dp = [[[0 for l in range(10)] for m in range(10)] for o in range(10)]
                dp[i][j][k] = 1
                for l in range(n):
                    dp2 = [[[0 for q in range(10)] for r in range(10)] for s in range(10)]
                    for q in range(10):
                        for r in range(10):
                            for s in range(10):
                                if dp[q][r][s] == 0:
                                    continue
                                if l == n-1:
                                    dp2[(q+a[l])%10][r][s] += dp[q][r][s]
                                    dp2[q][(r+a[l])%10][s] += dp[q][r][s]
                                else:
                                    dp2[(q+a[l])%10][r][s] += dp[q][r][s]
                                    dp2[q][(r+a[l])%10][s] += dp[q][r][s]
                                    dp2[q][r][(s+a[l])%10] += dp[q][r][s]
                                    dp2[(q*a[l])%10][r][s] += dp[q][r][s]
                                    dp2[q][(r*a[l])%10][s] += dp[q][r][s]
                                    dp2[q][r][(s*a[l])%10] += dp[q][r][s]
                    dp = dp2
                ans[k] += dp2[0][0][k]
    for i in range(10):
        print(ans[i]%mod)
