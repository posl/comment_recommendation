Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def divisors(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return divs

=======
Suggestion 6

def main():
    A, B = map(int, input().

=======
Suggestion 7

def main():
    from math import gcd
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(len([i for i in range(1, g + 1) if g % i == 0]))

=======
Suggestion 8

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

a,b=map(int,input().split())
g=gcd(a,b)
print(len([i for i in range(1,g+1) if g%i==0]))

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    # 約数を求める
    def divisor(n):
        i = 1
        res = []
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
            i += 1
        return res
    # AとBの約数の中で、AとBの最大公約数を含むものを求める
    res = divisor(A)
    res = [i for i in res if B % i == 0]
    # 最大公約数を除く
    res.remove(gcd(A, B))
    print(len(res))
