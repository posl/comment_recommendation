Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += a[i] * a[j]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        ans += pow(2, n-i, 998244353) * pow(2, i-1, 998244353) * a[i-1]
        ans %= 998244353
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    mod = 998244353

    #dp[i][j]表示前i个数中选出j个数的方案数
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(N+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*i

    #ans[i]表示前i个数的方案数
    ans = [0 for _ in range(N+1)]
    for i in range(N+1):
        for j in range(i+1):
            ans[i] += dp[i][j]*pow(2, N-i, mod)

    res = 0
    for i in range(N):
        if A[i] == 1:
            res += ans[N-i]
            res %= mod
    print(res)

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            avg = sum(a[j:j+i]) / i
            if avg == int(avg):
                ans += 1
    print(ans)

=======
Suggestion 5

def func(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j + 1]) % len(a[i:j + 1]) == 0:
                ans += 1
    return ans

=======
Suggestion 6

def getAvg(arr):
    return sum(arr) / len(arr)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        s = 0
        c = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j]
                c += 1
        if s % c == 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j+1]) % (j - i + 1) == 0:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 2**N):
        sum = 0
        count = 0
        for j in range(N):
            if (i>>j)&1:
                sum += A[j]
                count += 1
        if sum % count == 0:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 2**N):
        sum = 0
        for j in range(N):
            if ((i >> j) & 1):
                sum += A[j]
        if (sum % (i.bit_length()) == 0):
            cnt += 1
    print(cnt)
