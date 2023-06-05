Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    if K == 1:
        print(N+1)
    else:
        print((N+1)*(N+2)//2)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += i*(2*n-i+1)//2 - i*(i-1)//2 + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def f(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    else:
        return f(n - 1, k) + f(n - 1, k - 1)

n, k = map(int, input().split())
print(f(n, k) % 1000000007)

=======
Suggestion 4

def solve():
    # 读入数据
    N, K = map(int, input().split())

    # 计算答案
    # 由于10 ^ 100 + 1 <= 10 ^ 100 + 2 <= ... <= 10 ^ 100 + N
    # 所以，我们可以将问题转换为：
    # 从10 ^ 100 + 1，...，10 ^ 100 + N中选择K-1个整数，以使其和为X
    # 由于10 ^ 100 + 1 <= 10 ^ 100 + 2 <= ... <= 10 ^ 100 + N
    # 所以，我们可以将问题转换为：
    # 从1，...，N中选择K-1个整数，以使其和为X
    # 由于 1 <= K <= N + 1
    # 所以，我们可以将问题转换为：
    # 从1，...，N中选择K个整数，以使其和为X-K

    # 由于 1 <= K <= N + 1
    # 所以，我们可以将问题转换为：
    # 从1，...，N中选择K个整数，以使其和为X-K

    # 由于 1 <= N <= 2×10^5
    # 所以，我们可以将问题转换为：
    # 从1，...，2×10^5中选择K个整数，以使其和为X-K

    # 由于 1 <= K <= N + 1
    # 所以，我们可以将问题转换为：
    # 从1，...，2×10^5中选择K个整数，以使其和为X-K

    # 由于 1 <= X-K <= 2×10^5
    # 所以，我们可以将问题转换为：
    # 从1，...，2×10^5中选择K个整数，以使其和为X-K

    # 由于 1 <= K <= N + 1
    # 所以，我们可以将问题转换为：
    # 从1，

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    if n == k:
        print(1)
    else:
        print(((n - k + 1) * (n + k) // 2) % mod)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    if k == 1:
        print(n+1)
        return
    if k == 2:
        print((n+1)*(n+2)//2%mod)
        return
    if k == n+1:
        print(1)
        return
    if k == n:
        print(n+1)
        return
    if k == n-1:
        print((n+1)*(n+2)//2%mod)
        return
    if k == n-2:
        print((n+1)*(n+2)*(n+3)//6%mod)
        return
    print(1)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    if k == 1:
        print((n+1)%1000000007)
    elif k == n+1:
        print(1%1000000007)
    else:
        print((n*(n+1)//2 - (k-1)*k//2 + 1)%1000000007)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        min_sum = (i-1)*i//2
        max_sum = (N + N - i + 1) * i // 2
        ans += max_sum - min_sum + 1
        ans %= MOD
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int, input().split())
    #n,k = 200000,200001
    #n,k = 141421,35623
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        min = (i-1)*i//2
        max = (2*n-i+1)*i//2
        ans += max-min+1
        ans %= mod
    print(ans)
