Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x):
    return len(str(x))

n = int(input())
ans = 0
mod = 998244353
for i in range(1, n+1):
    ans += i
    ans %= mod
    if i == n:
        break
    if f(i) == f(i+1):
        continue
    else:
        ans += i
        ans %= mod
print(ans)

=======
Suggestion 2

def f(x):
    if x==0:
        return 0
    else:
        return 1+f(x//10)

N=int(input())
mod=998244353
ans=0
for i in range(1,10):
    if i<=N:
        ans+=i
    else:
        break
for i in range(1,18):
    if 10**i<=N:
        ans+=i*(min(N,10**(i+1)-1)-10**i+1)
    else:
        break
for i in range(1,18):
    if 10**i<=N:
        ans+=(10**i-1)//9
    else:
        break
print(ans%mod)

=======
Suggestion 3

def main():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n < 10 ** i:
            ans += i * (n - 10 ** (i - 1) + 1)
            break
        else:
            ans += i * (10 ** i - 10 ** (i - 1))
    print(ans % mod)

=======
Suggestion 4

def solve(n):
    mod = 998244353
    ans = 0
    x = 1
    while x <= n:
        y = min(n, x * 10 - 1)
        ans += (x + y) * (y - x + 1) // 2 * len(str(x))
        ans %= mod
        x *= 10
    return ans

=======
Suggestion 5

def main():
    n = int(input())
    print(solve(n))

=======
Suggestion 6

def problem238_c():
    print("problem238_c")
    return

=======
Suggestion 7

def f(x):
    return x

N = int(input())
print(f(N))

=======
Suggestion 8

def f(x):
    if x < 10:
        return x
    else:
        return 1 + f(x // 10)

=======
Suggestion 9

def problem238_c():
    print("238_c")
    N = int(input())
    print(N)

=======
Suggestion 10

def f(x):
    if x < 10:
        return x
    else:
        return 1 + f(x//10)

n = int(input())
mod = 998244353
ans = 0
for i in range(1, n+1):
    ans += f(i)
    ans %= mod
print(ans)
