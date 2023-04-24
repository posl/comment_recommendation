Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 2

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(a[0])
    else:
        ans = a[0]
        for i in range(1, n - 1):
            ans = gcd(ans, a[i])
        print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(gcd_list(A))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 最小公倍数を求める
    from fractions import gcd
    from functools import reduce
    def lcm_base(x, y):
        return (x * y) // gcd(x, y)

    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)

    # 最小公倍数を求める
    ans = lcm(*A)

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans = ans ^ a
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 体力が最小のモンスターを選ぶ
    minA = min(A)

    # 体力が最小のモンスターの体力を出力
    print(minA)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最小値を求める問題なので、最大公約数を求める
    from fractions import gcd
    from functools import reduce
    print(reduce(gcd, A))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最小公倍数を求める
    # 1. 2つの数の最大公約数を求める
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    # 2. 2つの数の最小公倍数を求める
    def lcm(a, b):
        return a*b//gcd(a,b)
    # 3. 3つ以上の数の最小公倍数を求める
    def lcmm(*args):
        return functools.reduce(lcm, args)
    print(lcmm(*A))
