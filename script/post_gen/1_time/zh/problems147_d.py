Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j]>>i)&1:
                cnt += 1
        ans += (cnt*(N-cnt)*(1<<i))%mod
    print(ans%mod)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j]>>i)&1:
                cnt += 1
        ans += cnt*(N-cnt)*(1<<i)
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1<<i):
                cnt += 1
        ans += cnt*(N-cnt)*(1<<i)
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        x = 0
        for j in range(N):
            if A[j]>>i & 1:
                x += 1
        ans += (1<<i)*x*(N-x)
        ans %= mod
    print(ans)

=======
Suggestion 5

def solve():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 3
    A = [1,2,3]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += A[i]^A[j]
    print(ans)
    return 0

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & 1:
                cnt += 1
            a[j] >>= 1
        ans += cnt * (n - cnt) * pow(2, i, mod)
        ans %= mod
    print(ans)
solve()

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if A[j] & (1<<i):
                cnt += 1
        ans += cnt*(N-cnt)*(1<<i)
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve(n, a):
    ans=0
    for i in range(60):
        one=0
        for j in range(n):
            if a[j]>>i & 1:
                one+=1
        ans+=one*(n-one)*(1<<i)
    return ans%((10**9)+7)

n=int(input())
a=list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 9

def main():
    from sys import stdin
    readline = stdin.readline

    N = int(readline())
    A = list(map(int, readline().split()))

    MOD = 10**9 + 7
    # 二进制表示的各位上的1的个数
    bit1 = [0] * 60
    for a in A:
        for i in range(60):
            bit1[i] += a >> i & 1

    ans = 0
    for i in range(60):
        # 2^i位上的1的个数
        n = bit1[i]
        # 2^i位上的1的个数 * 2^(N-1-i)个数
        ans += n * (N - n) * pow(2, i, MOD)
        ans %= MOD

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * (1 << i)
    print(ans % (10 ** 9 + 7))
    return
