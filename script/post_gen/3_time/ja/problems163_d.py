Synthesizing 10/10 solutions

=======
Suggestion 1

def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    numer = 1  # 分子
    denom = 1  # 分母
    for i in range(1, r + 1):
        numer = numer * (n + 1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod

mod = 10**9+7
n, k = map(int, input().split())
print(cmb(n+k, k, mod))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += i * (2 * N - i + 1) // 2 - i * (i - 1) // 2 + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i + 1
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    mod = pow(10, 9) + 7
    ans = 0
    for i in range(k, n + 2):
        ans += (n - i + 1) * (n + i + 1) // 2 - (i - 1) * i // 2 + 1
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        min = i*(i-1)//2
        max = i*(2*n-i+1)//2
        ans += max - min + 1
        ans %= mod
    print(ans)

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += i*N - i*(i-1) + 1
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    a = [0] * (n+2)
    b = [0] * (n+2)
    a[0] = 1
    b[0] = 1
    for i in range(1, n+2):
        a[i] = (a[i-1] * i) % mod
        b[i] = pow(a[i], mod-2, mod)
    ans = 0
    for i in range(k):
        ans += a[n+1] * b[i] * b[n+1-i] % mod
        ans %= mod
    print(ans)

=======
Suggestion 9

def combination_mod(n, r, mod):
    if n < r:
        return 0
    elif n < 0 or r < 0:
        return 0
    elif n == 0 or r == 0:
        return 1
    else:
        return (fact[n] * factinv[r] * factinv[n-r]) % mod

n,k = map(int,input().split())
mod = 10**9+7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, n+k+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[i]) % mod)

ans = 0
for i in range(k,n+2):
    ans += combination_mod(n+1,i,mod)*combination_mod(n,i-1,mod)
    ans %= mod

print(ans)

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    sum = 0
    for i in range(2, N + 2):
        sum += i
        if i >= K:
            ans += sum - (i - K) - 1
            ans %= mod
    print(ans)
