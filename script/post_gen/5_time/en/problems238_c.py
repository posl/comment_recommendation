Synthesizing 10/10 solutions

=======
Suggestion 1

def count_digits(n):
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits

=======
Suggestion 2

def f(x):
    if x < 10:
        return x
    else:
        return x % (10 ** len(str(x)))

N = int(input())
sum = 0
for i in range(1, N + 1):
    sum += f(i)
print(sum % 998244353)

=======
Suggestion 3

def get_digits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits[::-1]

=======
Suggestion 4

def problem238_c():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n >= 10 ** i:
            ans += 9 * pow(10, i - 1, mod)
        else:
            ans += (n - 10 ** (i - 1) + 1) * pow(10, i - 1, mod)
            break
    print(ans % mod)

=======
Suggestion 5

def f(x):
    if x < 10:
        return x
    else:
        return x // 10 + 9

=======
Suggestion 6

def f(x):
    return x - 10**(len(str(x))-1) + 1

=======
Suggestion 7

def f(x):
    if x < 10:
        return x
    else:
        return 9 + f(x//10) - 1

=======
Suggestion 8

def main():
    N = int(input())
    mod = 998244353
    ans = 0
    tmp = 10
    while tmp <= N:
        ans += (N//tmp)*(tmp//10)
        ans += max(0, (N%tmp) - (tmp//10) + 1)
        ans %= mod
        tmp *= 10
    print(ans)

=======
Suggestion 9

def solve(n):
    if n < 10:
        return n
    else:
        return 9 + (n-10)//10

=======
Suggestion 10

def f(x):
    return x*(x+1)//2
