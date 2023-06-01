Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n,a,b = map(int,input().split())
g = gcd(a,b)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, a, b = map(int, input().split())
g = gcd(a, b)
a //= g
b //= g
p = 10 ** 9 + 7

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 5

def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b

=======
Suggestion 6

def main():
    # 读入
    n, a, b = map(int, input().split())
    # 两个数的最大公约数
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    # 两个数的最小公倍数
    def lcm(x, y):
        return x * y // gcd(x, y)
    # 两个数的最小公倍数的倍数
    l = lcm(a, b)
    # 两个数的最小公倍数的倍数的个数
    m = n // l
    # 两个数的最小公倍数的倍数的最大个数
    max = 2 * m
    # 两个数的最小公倍数的倍数的最小个数
    min = 2 * m - 1
    # 两个数的最小公倍数的倍数的个数的差
    d = max - min
    # 两个数的最小公倍数的倍数的最小个数的最大值
    max_min = max + d * (n % l == 0)
    # 两个数的最小公倍数的倍数的最大个数的最小值
    min_max = min - d * (n % l == 0)
    # 两个数的最小公倍数的倍数的个数的和
    sum = (max_min + min_max) * (n // l) // 2
    # 两个数的最小公倍数的倍数的个数的和的差
    diff = max_min - min_max
    # 两个数的最小公倍数的倍数的个数的和的差的最小值
    min_sum = sum - diff * (n % l == 0)
    # 两个数的最小公倍数的倍数的个数的和的差的最大值
    max_sum = sum + diff * (n % l == 0)
    # 两个数的最小公倍数的倍数的个数的和

=======
Suggestion 7

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 8

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 9

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
