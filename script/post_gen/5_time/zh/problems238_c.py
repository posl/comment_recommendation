Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    return len(str(x))

=======
Suggestion 2

def f(x):
    return x

=======
Suggestion 3

def f(x):
    return int(x*(10**(len(str(x)))-1)/9)
N = int(input())
ans = 0
for i in range(1,10):
    if f(i) <= N:
        ans += i
    else:
        ans += N - 10**(len(str(i))-1) + 1
        break
print(ans%998244353)

=======
Suggestion 4

def f(x):
    if x < 10:
        return x
    else:
        return f(x // 10) + 1

n = int(input())
ans = 0
mod = 998244353

for i in range(1, n + 1):
    ans += f(i)
    ans %= mod

print(ans)

=======
Suggestion 5

def getSum(N):
    n = len(str(N))
    sum = 0
    for i in range(1,n):
        sum += i * 9 * (10 ** (i-1))
    sum += n * (N - 10 ** (n-1) + 1)
    return sum

N = int(input())
print(getSum(N) % 998244353)

=======
Suggestion 6

def main():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n < 10**i:
            ans += (n - 10**(i-1) + 1) * i
            break
        else:
            ans += (10**i - 10**(i-1)) * i
    print(ans % mod)

=======
Suggestion 7

def f(x):
    return x if x < 10 else 1 + f(x // 10)

N = int(input())
MOD = 998244353

ans = 0
for i in range(1, 19):
    l = 10 ** (i - 1)
    r = min(N, 10 ** i - 1)
    if l <= N:
        ans += (r + l) * (r - l + 1) // 2 * i
        ans %= MOD
print(ans)

=======
Suggestion 8

def f(n):
    if n < 10:
        return n
    else:
        return f(n - 1) + 1

n = int(input())
print (f(n) % 998244353)
