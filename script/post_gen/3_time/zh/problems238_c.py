Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    return x

=======
Suggestion 2

def f(x):
    if x < 10:
        return x
    else:
        return f(x // 10) + 1

=======
Suggestion 3

def get_modulo_sum(N):
    # 998244353
    modulo = 998244353
    # 位数
    digit = len(str(N))
    # 位数が一桁の場合
    if digit == 1:
        return N
    # 位数が二桁以上の場合
    # 位数が一桁少ない桁数の最大値
    max_digit = int('9' * (digit - 1))
    # 位数が一桁少ない桁数の最大値までの和
    sum = 0
    for i in range(1, max_digit + 1):
        sum += i
    # 位数が一桁少ない桁数の最大値までの和に、位数が一桁少ない桁数の最大値をかける
    sum *= max_digit
    # 位数が一桁少ない桁数の最大値までの和に、位数が一桁少ない桁数の最大値までの和を足す
    sum += get_modulo_sum(max_digit)
    # 位数が一桁少ない桁数の最大値までの和に、位数が一桁少ない桁数の最大値までの和を足す
    sum %= modulo
    # 位数が一桁少ない桁数の最大値に、Nと位数が一桁少ない桁数の最大値の差をかける
    sum += max_digit * (N - max_digit)
    # 位数が一桁少ない桁数の最大値に、Nと位数が一桁少ない桁数の最大値の差を足す
    sum %= modulo
    # 位数が一桁少ない桁数の最大値に、Nと位数が一桁少ない桁数の最大値の差を足す
    sum += get_mod

=======
Suggestion 4

def solve(N):
    # N = 16
    # N = 238
    # N = 999999999999999999
    # N = 1000000000000000000
    # N = 1000000000000000001
    # N = 1000000000000000002
    # N = 1000000000000000003
    # N = 1000000000000000004
    # N = 1000000000000000005
    # N = 1000000000000000006
    # N = 1000000000000000007
    # N = 1000000000000000008
    # N = 1000000000000000009
    # N = 1000000000000000010
    # N = 1000000000000000011
    # N = 1000000000000000012
    # N = 1000000000000000013
    # N = 1000000000000000014
    # N = 1000000000000000015
    # N = 1000000000000000016
    # N = 1000000000000000017
    # N = 1000000000000000018
    # N = 1000000000000000019
    # N = 1000000000000000020
    # N = 1000000000000000021
    # N = 1000000000000000022
    # N = 1000000000000000023
    # N = 1000000000000000024
    # N = 1000000000000000025
    # N = 1000000000000000026
    # N = 1000000000000000027
    # N = 1000000000000000028
    # N = 1000000000000000029
    # N = 1000000000000000030
    # N = 1000000000000000031
    # N = 1000000000000000032
    # N = 1000000000000000033
    # N = 1000000000000000034
    # N = 1000000000000000035
    # N

=======
Suggestion 5

def f(x):
    return x

N = int(input())
ans = 0
for k in range(1, N+1):
    ans += f(k)
print(ans % 998244353)

=======
Suggestion 6

def f(x):
    return x

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += f(i)
    ans %= 998244353

print(ans)

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
for i in range(1, 19):
    if 10**i > N:
        break
    ans += (min(10**i-1, N) - 10**(i-1) + 1) * f(10**(i-1))
    ans %= mod
print(ans)

=======
Suggestion 8

def f(x):
    return x

N = int(input())

sum = 0
for i in range(1, N+1):
    sum += f(i)

print(sum % 998244353)

=======
Suggestion 9

def f(x):
    s = str(x)
    return len(s)

N = int(input())
mod = 998244353

ans = 0
for i in range(1, N+1):
    ans += i * f(i)
    ans %= mod

print(ans)
