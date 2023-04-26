Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())
for i in range(C, D+1):
    if is_prime(A+i):
        print('Takahashi')
        exit()
print('Aoki')

=======
Suggestion 3

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

=======
Suggestion 4

def main():
    A, B, C, D = map(int, input().split())
    if B < C or D < A:
        print("Aoki")
    else:
        print("Takahashi")

=======
Suggestion 5

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())

for i in range(A, B+1):
    for j in range(C, D+1):
        if isPrime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

=======
Suggestion 6

def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

A, B, C, D = map(int, input().split())

=======
Suggestion 7

def isPrime(n): #素数判定
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())

=======
Suggestion 8

def main():
    A, B, C, D = map(int, input().split())
    if A <= 2 and C <= 2:
        print('Aoki')
    else:
        print('Takahashi')

=======
Suggestion 9

def main():
    A, B, C, D = map(int, input().split())
    # A以上B以下の整数の和が素数であるかどうかを判定する
    # A以上B以下の整数の和は、
    # 1以上B以下の整数の和から1以上A-1以下の整数の和を引けば求めることができる
    # 1以上B以下の整数の和は、
    # B以下の素数の個数にBを掛けたものに、
    # B以下の合成数の個数にBを掛けたものを加えたものになる
    # つまり、B以下の合成数の個数を求めれば良い
    # 1以上B以下の合成数の個数は、
    # 1以上B以下の整数のうち、B以下の素数の倍数の個数に、
    # 1以上B以下の整数のうち、B以下の素数の2乗以上の倍数の個数を加えたものになる
    # つまり、B以下の素数の倍数の個数とB以下の素数の2乗以上の倍数の個数を求めれば良い
    # 1以上B以下の素数の倍数の個数は、
    # B以下の素数の個数にB以下の素数の個数を掛けたものになる
    # つまり、B以下の素数の個数を求めれば良い
    # 1以上B以下の素数の個数は、
    # B以下の素数のリストの長さになる
    # 1以上B以下の素数のリストを求めるにはエラトステネスの篩を使う
    # 1以上B以下の素数の2乗以上の倍数の個数は、
    # B
