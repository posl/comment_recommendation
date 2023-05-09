Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        ans[i] = 1 if i == A[-1] else 0
    for i in range(N-2, -1, -1):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + A[i]) % 10] = (tmp[(j + A[i]) % 10] + ans[j]) % MOD
            tmp[(j * A[i]) % 10] = (tmp[(j * A[i]) % 10] + ans[j]) % MOD
        ans = tmp
    print(*ans, sep="\n")

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N - 1):
            a = A[j]
            b = A[j + 1]
            if (a + b) % 10 == i:
                A[j + 1] = (a + b) % 10
            else:
                A[j + 1] = (a * b) % 10
        ans[i] = A[N - 1]
        A = list(map(int, input().split()))
    print(*ans, sep="\n")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0 for _ in range(10)]
    ans[A[0]] = 1
    for a in A[1:]:
        tmp = [0 for _ in range(10)]
        for j in range(10):
            tmp[(j + a) % 10] += ans[j]
            tmp[(j * a) % 10] += ans[j]
            tmp[(j + a) % 10] %= 998244353
            tmp[(j * a) % 10] %= 998244353
        ans = tmp
    for a in ans:
        print(a % 998244353)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        ans[i] = A.count(i)
    for i in range(N - 1):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j + A[i + 1]) % 10] += ans[j]
            ans2[(j + A[i + 1]) % 10] %= mod
            ans2[(j * A[i + 1]) % 10] += ans[j]
            ans2[(j * A[i + 1]) % 10] %= mod
        ans = ans2
    for i in range(10):
        print(ans[i])
solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*10
    ans[A[0]] = 1
    for i in range(1,N):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+A[i])%10] += ans[j]
            tmp[(j*A[i])%10] += ans[j]
        ans = tmp
    for i in ans:
        print(i%998244353)

=======
Suggestion 6

def solve(N, A):
    mod = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        new_ans = [0] * 10
        for j in range(10):
            new_ans[(j + A[i]) % 10] += ans[j]
            new_ans[(j * A[i]) % 10] += ans[j]
        for j in range(10):
            new_ans[j] %= mod
        ans = new_ans
    return ans

N = int(input())
A = list(map(int, input().split()))
ans = solve(N, A)
print("\n".join(map(str, ans)))

=======
Suggestion 7

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #compute
    MOD = 998244353
    dp = [0]*10
    dp[A[0]] = 1
    for i in range(1, N):
        dp2 = [0]*10
        for j in range(10):
            dp2[(j+A[i])%10] += dp[j]
            dp2[(j*A[i])%10] += dp[j]
        for j in range(10):
            dp[j] = dp2[j] % MOD
    #output
    print(*dp, sep='\n')

=======
Suggestion 8

def f(x,y):
    return (x+y)%10

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def get_int():
    return int(input())
