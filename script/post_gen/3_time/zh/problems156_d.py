Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
g = gcd(a, b)
a //= g
b //= g
ans = pow(2, n, mod) - 1
c1 = c2 = 1
for i in range(b):
    c1 = c1 * (n - i) * pow(i + 1, mod - 2, mod) % mod
for i in range(a):
    c2 = c2 * (n - i) * pow(i + 1, mod - 2, mod) % mod
ans = (ans - c1 - c2) % mod
print(ans)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n, a, b = map(int, input().split())
g = gcd(a, b)
a //= g
b //= g
m = min(a, b)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    if n == 2:
        print(0)
        exit()
    if a == 1:
        if b == 2:
            print(0)
            exit()
        else:
            print(1)
            exit()
    if b == n:
        print(0)
        exit()
    if a == 2:
        if b == 3:
            print(0)
            exit()
        else:
            print(1)
            exit()
    if b == n - 1:
        print(0)
        exit()
    if b - a == 1:
        print(0)
        exit()
    if a == b:
        print(1)
        exit()
    if b - a == 2:
        print(1)
        exit()
    if b - a == 3:
        print(2)
        exit()
    if b - a == 4:
        print(4)
        exit()
    if b - a == 5:
        print(7)
        exit()
    if b - a == 6:
        print(13)
        exit()
    if b - a == 7:
        print(24)
        exit()
    if b - a == 8:
        print(44)
        exit()
    if b - a == 9:
        print(81)
        exit()
    if b - a == 10:
        print(149)
        exit()
    if b - a == 11:
        print(274)
        exit()
    if b - a == 12:
        print(504)
        exit()
    if b - a == 13:
        print(927)
        exit()
    if b - a == 14:
        print(1705)
        exit()
    if b - a == 15:
        print(3136)
        exit()
    if b - a == 16:
        print(5768)
        exit()
    if b - a == 17:
        print(10609)
        exit()
    if b - a == 18:
        print(19513)
        exit()
    if b - a == 19:
        print(35890)
        exit()
    if b - a == 20:
        print(66012)
        exit()

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

=======
Suggestion 5

def find_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return find_gcd(b, a%b)

=======
Suggestion 6

def solve(n, a, b):
    MOD = 10 ** 9 + 7
    # 1. nCkを求める
    # 2. nCkから、aCkとbCkを引く
    # 3. 2で求めた値をnCkから引く
    # 4. 3で求めた値をMODで割る
    def comb(n, k):
        x, y = 1, 1
        for i in range(k):
            x *= n - i
            y *= i + 1
            x %= MOD
            y %= MOD
        return x * pow(y, MOD - 2, MOD)

    ans = pow(2, n, MOD) - comb(n, a) - comb(n, b)
    return ans % MOD

n, a, b = map(int, input().split())
print(solve(n, a, b))

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    if n < 2 * 10 ** 5:
        ans = pow(2, n, 10 ** 9 + 7) - 1
        ans -= comb(n, a)
        ans -= comb(n, b)
        print(ans % (10 ** 9 + 7))
    else:
        pass

=======
Suggestion 8

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 9

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
