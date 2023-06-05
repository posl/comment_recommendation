Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (N - cnt) * (1 << i)) % (10**9 + 7)
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j]>>i & 1:
                cnt += 1
        ans += cnt * (n-cnt) * pow(2, i, mod)
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 10
    a = [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        ans += cnt * (n-cnt) * (1 << i)
        ans %= mod
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 0
    for i in range(60):
        mask = 1 << i
        count = 0
        for j in range(n):
            if a[j] & mask:
                count += 1
        ans += (count * (n-count) * mask) % MOD
    print(ans % MOD)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (1 << i) * cnt * (n - cnt)
        ans %= 1000000007
    print(ans)

=======
Suggestion 6

def get_xor_sum(n, a_list):
    xor_sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            xor_sum += a_list[i] ^ a_list[j]
    return xor_sum

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j]>>i & 1:
                cnt += 1
        ans += cnt*(n-cnt)*(1<<i)
        ans %= mod
    print(ans)

solve()

=======
Suggestion 8

def solve():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(60):
        x=0
        for j in range(n):
            if a[j]>>i&1:
                x+=1
        ans+=x*(n-x)*(1<<i)
        ans%=1000000007
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7

    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += (cnt * (n - cnt) * (1 << i)) % mod
        ans %= mod
    print(ans)

=======
Suggestion 10

def get_xor_sum(a):
    xor_sum = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            xor_sum += a[i] ^ a[j]
    return xor_sum
