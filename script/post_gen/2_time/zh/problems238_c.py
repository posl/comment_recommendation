Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(f(N))

=======
Suggestion 2

def main():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 18):
        if n < 10**i:
            ans += (n - 10**(i-1) + 1) * i
            break
        else:
            ans += (10**i - 10**(i-1)) * i
    print(ans % mod)

=======
Suggestion 3

def main():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n < 10 ** i:
            ans += (n - 10 ** (i - 1) + 1) * i
            break
        else:
            ans += (10 ** i - 10 ** (i - 1)) * i
    ans %= mod
    print(ans)

=======
Suggestion 4

def f(x):
    return len(str(x))

=======
Suggestion 5

def f(x):
    if x < 10:
        return x
    else:
        return f(x//10) + 1

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += f(i)
    ans %= 998244353
print(ans)

=======
Suggestion 6

def f(x):
    return x

=======
Suggestion 7

def f(x):
    if x < 10:
        return x
    else:
        return f(x//10) + 1

N = int(input())
mod = 998244353
ans = 0
for i in range(1, N+1):
    ans += f(i)
    ans %= mod
print(ans)

=======
Suggestion 8

def get_digits(n):
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits

=======
Suggestion 9

def calc(N):
    if N < 10:
        return N
    else:
        s = str(N)
        l = len(s)
        first = int(s[0])
        if first == 1:
            return calc(10 ** (l - 1) - 1) + calc(N - 10 ** (l - 1))
        else:
            return first * calc(10 ** (l - 1) - 1) + calc(N - first * (10 ** (l - 1)))

N = int(input())
print(calc(N) % 998244353)
