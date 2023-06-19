Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k,n+2):
        ans = (ans + (n-i+1)*i +1) % mod
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        min_sum = i * (i - 1) // 2
        max_sum = i * (2 * 10**100 + i - 1) // 2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    if k>n:
        print(0)
        return
    if k==n:
        print(1)
        return
    if k==n-1:
        print(n)
        return
    ans = 0
    for i in range(k,n+1):
        ans += i*(n-i+1)+1
    print(ans%mod)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    if k == n+1:
        print(1)
        return
    if k == 2:
        print(n*(n+1)//2)
        return
    if k == 3:
        print(n*(n+1)*(n+2)//6)
        return
    if k == 4:
        print(n*(n+1)*(n+2)*(n+3)//24)
        return
    if k == 5:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)//120)
        return
    if k == 6:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)//720)
        return
    if k == 7:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)//5040)
        return
    if k == 8:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)//40320)
        return
    if k == 9:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)//362880)
        return
    if k == 10:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)*(n+9)//3628800)
        return
    if k == 11:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)*(n+9)*(n+10)//39916800)
        return
    if k == 12:
        print(n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)*(n+9)*(n+10)*(n+11)//479001600)
        return
    if k == 13:
        print(n*(n+1)*(n+2)*(n+3)*(

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    if N == K - 1:
        print(1)
    else:
        ans = 0
        for i in range(K, N + 2):
            ans += (N + 1) * i - i * (i - 1) // 2 + 1
            ans %= mod
        print(ans)

=======
Suggestion 6

def solve(n,k):
    mod=10**9+7
    sum=0
    for i in range(k,n+2):
        min=i*(i-1)//2
        max=i*(2*n-i+1)//2
        sum=(sum+max-min+1)%mod
    return sum

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        min = (i-1)*i//2
        max = (2*n-i+1)*i//2
        ans += max - min + 1
        ans %= mod
    print(ans)

=======
Suggestion 8

def func(n, k):
    if k == 1:
        return n
    elif k == n + 1:
        return 1
    else:
        return n * (n + 1) // 2 - k + 1


n, k = map(int, input().split())
print(func(n, k) % (10 ** 9 + 7))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    if n == k-1:
        print(1)
        return
    elif n < k-1:
        print(0)
        return
    else:
        ans = 0
        for i in range(k, n+2):
            min = i*(i-1)//2
            max = i*(2*n-i+1)//2
            ans += max-min+1
            ans %= mod
        print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n + 2):
        ans += (n - i + 1) * i + 1
        ans %= mod
    print(ans)
