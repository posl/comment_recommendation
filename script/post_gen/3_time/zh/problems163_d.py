Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(N, K):
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += N * i + 1 - i * (i-1) // 2
        ans %= MOD
    return ans

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(k, n + 2):
        ans += (n - i + 1) * (n + i + 1) // 2 - (n - i + 1) * i + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        min_sum = (i-1)*i//2
        max_sum = (2*n-i+1)*i//2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def problems163_d():
    pass

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    print(ans)
main()

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k,n+2):
        ans += i*(n-i+1)+1
        ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    #读取输入
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    #如果k>n+1的话，那么必须选n+1个数，这时候只有一种可能，就是所有的数都选上
    if k > n + 1:
        k = n + 1
    #计算最小和
    min_sum = 0
    for i in range(k):
        min_sum += 10 ** 100 + i
    #计算最大和
    max_sum = 0
    for i in range(n, n - k, -1):
        max_sum += 10 ** 100 + i
    #计算和的可能种类数
    count = max_sum - min_sum + 1
    #输出结果
    print(count % mod)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        min = (i-1)*i//2
        max = (2*N-i+1)*i//2
        ans += max - min + 1
        ans %= mod
    print(ans)
