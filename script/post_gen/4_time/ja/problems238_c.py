Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_digit(n):
    digit = 0
    while n != 0:
        n //= 10
        digit += 1
    return digit

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += len(str(i))
    print(ans % 998244353)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += len(str(i))
    print(ans % 998244353)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += len(str(i)) * (n // i)
        ans %= 998244353
    print(ans)

=======
Suggestion 5

def f(x):
    return len(str(x))

=======
Suggestion 6

def main():
    N = int(input())
    # 10^n 以下の整数で、桁数が n 桁のものの個数
    # 1桁: 9
    # 2桁: 90
    # 3桁: 900
    # 4桁: 9000
    # ... とな�

=======
Suggestion 7

def count_digits(num):
    return len(str(num))
