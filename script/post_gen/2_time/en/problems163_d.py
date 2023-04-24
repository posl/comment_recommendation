Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (i * (N + N - i + 1) // 2) - (i * (i - 1) // 2) + 1
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(k, n + 2):
        a = i * (n - i + 1) + 1
        b = i * (i - 1) // 2
        ans += a - b
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (i * (N-i+1) + 1)
    print(ans%MOD)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (i + N) * (N - i + 1) // 2 + 1
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (N + i + 1) * i // 2 - N * (i - 1)
    print(ans % MOD)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min_sum = i * (i-1) // 2
        max_sum = N * (N+1) // 2 - (N-i) * (N-i-1) // 2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7

    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1
        ans %= MOD

    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (i*(n+1-i+1)+1)*(n+1-i+1)//2
        ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    def sum_of_arithmetic_series(first, last, n):
        return (first + last) * n // 2
    ans = 0
    for i in range(K, N + 2):
        ans += sum_of_arithmetic_series(10 ** 100, 10 ** 100 + i - 1, i) - sum_of_arithmetic_series(10 ** 100, 10 ** 100 + N - i, N - i + 1) + 1
        ans %= MOD
    print(ans)
