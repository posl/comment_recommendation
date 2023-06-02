Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    if K == 1:
        print(N+1)
        return
    if K == N+1:
        print(1)
        return
    if K == 2:
        print((N+1)*(N+2)//2)
        return
    if K >= N//2:
        K = N - K + 2
    print(K*(N-K+2))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        min_sum = i * (i - 1) // 2
        max_sum = i * (2 * n - i + 1) // 2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    if k == 1:
        print(n+1)
    else:
        ans = 0
        for i in range(k, n+2):
            ans += i*(n+1-i+1)+1
            ans %= mod
        print(ans)
main()

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += i * (N + N - i + 1) // 2 + 1
        ans %= mod
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        max_sum = i*(2*(10**100)+i-1)//2
        min_sum = (N+1-i)*(10**100 + N+1-i+1)//2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

=======
Suggestion 6

def solve(n,k):
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += n*i-i*(i-1)//2+1
        ans %= mod
    return ans

n,k = map(int,input().split())
print(solve(n,k))

=======
Suggestion 7

def solve():
    N,K = map(int,input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K,N+2):
        min = i*(i-1)//2
        max = i*(N+N-i+1)//2
        ans += max - min + 1
        ans %= MOD
    print(ans)

=======
Suggestion 8

def solve():
    N,K = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K,N+2):
        ans += (N+1-i)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 9

def f(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    return f(n-1, k) + f(n-1, k-1)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7

    # 从n+1个数中选k个，和的取值范围为[sum1, sum2]
    sum1 = sum([10 ** 100 + i for i in range(k)])
    sum2 = sum([10 ** 100 + i for i in range(n, n - k, -1)])

    # 用前缀和数组存储组合数
    prefix = [1 for i in range(sum2 - sum1 + 1)]
    for i in range(1, sum2 - sum1 + 1):
        prefix[i] = prefix[i - 1] * i % mod

    # 求逆元
    inverse = [1 for i in range(sum2 - sum1 + 1)]
    inverse[-1] = pow(prefix[-1], mod - 2, mod)
    for i in range(sum2 - sum1, 0, -1):
        inverse[i - 1] = inverse[i] * i % mod

    # 求组合数
    def comb(n, k, mod):
        if k == 0:
            return 1
        return prefix[n] * inverse[k] % mod * inverse[n - k] % mod

    print((comb(sum2 - sum1 + 1, k - 1, mod) - comb(sum2 - sum1 + 1, k, mod)) % mod)
