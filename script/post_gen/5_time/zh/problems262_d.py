Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum(a[i:j]) % (j - i) == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    an = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1 << n):
        sm = 0
        for j in range(n):
            if i & (1 << j):
                sm += an[j]
        if sm % 2 == 0:
            ans += 1
    print(ans % mod)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if (A[i] + A[j]) % 2 == 0:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    ans += 1

    print(ans)

=======
Suggestion 5

def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    return N, a

=======
Suggestion 6

def solve(n,a):
    #dp[i][j]表示前i个数中选j个数，这j个数的平均值是整数的情况数
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]
            if j-1 >= 0 and a[i-1] % j == 0:
                dp[i][j] += dp[i-1][j-1]
    res = 0
    for i in range(1,n+1):
        res += dp[n][i]
    return res

=======
Suggestion 7

def func(a):
    #print(a)
    if len(a) == 1:
        if a[0] % 2 == 0:
            return 1
        else:
            return 0
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        if sum % len(a) == 0:
            return 1
        else:
            return 0

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum(A[i:j]) % (j-i) == 0:
                ans += 1
    print(ans % mod)
solve()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
    ans = 0
    for i in range(N):
        if (sum % A[i] == 0):
            ans += 1
    print(ans)
    
main()

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    ans += 1
                else:
                    break
    print(ans)
