Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (N + 1) * (N + 2) // 2 - i * (i - 1) // 2 + 1
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N+1-i)*i + 1
    print(ans%mod)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0

    for i in range(k, n + 2):
        min_sum = i * (i - 1) // 2
        max_sum = i * (2 * n - i + 1) // 2
        ans += max_sum - min_sum + 1
        ans %= mod

    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min = i*(i-1)//2
        max = (N+i)*(N-i+1)//2
        ans += max - min + 1
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K,N+2):
        min_sum = i*(i-1)//2
        max_sum = i*(2*N-i+1)//2
        ans += (max_sum-min_sum+1)%mod
    print(ans%mod)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7

    ans = 0
    for i in range(k, n+2):
        ans += (i*(2*n+1-i)+1)//2
        ans %= mod

    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min_ = i * (i - 1) // 2
        max_ = i * (2 * N - i + 1) // 2
        ans += max_ - min_ + 1
        ans %= MOD
    print(ans)

main()

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    MOD = 10**9+7

    def comb(n, r, mod=MOD):
        if n < 0 or r < 0 or n < r:
            return 0
        r = min(r, n - r)
        if r == 0:
            return 1
        if r == 1:
            return n % mod
        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]
        for p in range(2, r + 1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p - 1, r, p):
                    numerator[k - offset] //= pivot
                    denominator[k] //= pivot
        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result = (result * numerator[k]) % mod
        return result

    ans = 0
    for i in range(K, N+2):
        ans += comb(N+1, i)
        ans %= MOD
    print(ans)

=======
Suggestion 9

def get_ints(): return map(int, input().strip().split())

=======
Suggestion 10

def get_input():
    return map(int, input().split())
