Synthesizing 10/10 solutions

=======
Suggestion 1

def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, len(str(N)) + 1):
        ans += (N // (10 ** i) * (10 ** (i - 1))) % MOD
        ans %= MOD
        ans += max(0, (N % (10 ** i)) - (10 ** (i - 1)) + 1) % MOD
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, len(str(N)) + 1):
        ans += (N - 10 ** (i - 1) + 1) * i
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += N//(10**i)*(10**(i-1))
        ans %= mod
        if N%(10**i) >= 10**(i-1):
            ans += 10**(i-1)
            ans %= mod
        else:
            ans += N%(10**i) + 1
            ans %= mod
    print(ans)

main()

=======
Suggestion 5

def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**(i-1))-10**(i-1)+1)*i
        ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, 19):
        ans += (N // (10 ** i)) * (10 ** i - 10 ** (i - 1))
        ans += max(0, (N % (10 ** i)) - (10 ** (i - 1)) + 1)
    print(ans % 998244353)

=======
Suggestion 7

def main():
    N = int(input())
    n = len(str(N))
    M = 998244353
    ans = 0
    for i in range(1,n):
        ans += 9*(10**(i-1))*i
        ans %= M
    ans += (N-(10**(n-1))+1)*n
    ans %= M
    print(ans)

=======
Suggestion 8

def solve(N):
    MOD = 998244353
    A = []
    while N > 0:
        A.append(N % 10)
        N //= 10
    A.reverse()
    ans = 0
    for i in range(1, len(A)):
        ans += 45 * pow(10, i - 1, MOD) * i
        ans %= MOD
    for i in range(len(A)):
        for j in range(1, A[i]):
            ans += pow(10, len(A) - i - 1, MOD) * (i + 1)
            ans %= MOD
        ans += sum(A[i + 1:]) + 1
        ans %= MOD
    return ans

N = int(input())
print(solve(N))

I got a WA on this problem. I'm not sure if I'm missing something, but I believe my code is correct.

I'm not sure if this is the right place to ask, but I'm having trouble with this problem. I've tried to write a recursive function to solve this, but I'm not sure if it's correct. I'd appreciate any help.

Here's my code:

=======
Suggestion 9

def  main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 19):
        l = 10 ** (i - 1)
        r = min(10 ** i - 1, N)
        ans += (r - l + 1) * i
        ans %= MOD
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    print(solve(N))
