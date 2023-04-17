Synthesizing 10/10 solutions

=======

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======

def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4
    if n == 5:
        return 5
    if n == 6:
        return 6
    if n == 7:
        return 7
    if n == 8:
        return 8
    if n == 9:
        return 9
    if n == 10:
        return 19
    if n == 11:
        return 29
    if n == 12:
        return 39
    if n == 13:
        return 49
    if n == 14:
        return 59
    if n == 15:
        return 69
    if n == 16:
        return 79
    if n == 17:
        return 89
    if n == 18:
        return 99
    if n == 19:
        return 199
    if n == 20:
        return 299
    if n == 21:
        return 399
    if n == 22:
        return 499
    if n == 23:
        return 599
    if n == 24:
        return 699
    if n == 25:
        return 799
    if n == 26:
        return 899
    if n == 27:
        return 999
    if n == 28:
        return 1999
    if n == 29:
        return 2999
    if n == 30:
        return 3999
    if n == 31:
        return 4999
    if n == 32:
        return 5999
    if n == 33:
        return 6999
    if n == 34:
        return 7999
    if n == 35:
        return 8999
    if n == 36:
        return 9999
    if n == 37:
        return 19999
    if n == 38:
        return 29999
    if n == 39:
        return 39999
    if n == 40:
        return 49999
    if n ==

=======

def main():
    k = int(input())
    snuke = []
    for i in range(1, 10):
        snuke.append(i)
    for i in range(k):
        print(snuke[i])
        if snuke[i] % 10 != 0:
            snuke.append(snuke[i] * 10 + snuke[i] % 10 - 1)
        snuke.append(snuke[i] * 10 + snuke[i] % 10)
        if snuke[i] % 10 != 9:
            snuke.append(snuke[i] * 10 + snuke[i] % 10 + 1)

=======

def is_snuke_number(n):
    m = n
    s = 0
    while m > 0:
        s += m % 10
        m = m // 10
    return n % s == 0

=======

def snuke(n):
    if n < 10:
        return n
    else:
        return snuke(n//10) + n%10

=======

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

=======

def sum_digits(n):
    return sum([int(i) for i in str(n)])

=======

def s(n):
    return sum(map(int, list(str(n))))

=======

def main():
    K = int(input())

    # K個の最小のSnuke数を列挙する
    # 1桁のSnuke数はすべてSnuke数
    # 2桁のSnuke数は1桁のSnuke数を1つ前にくっつけたもの
    # 3桁のSnuke数は2桁のSnuke数を1つ前にくっつけたもの
    # というように考えると、
    # 1桁のSnuke数のリスト
    # 2桁のSnuke数のリスト
    # 3桁のSnuke数のリスト
    # ...
    # を作成していけば良い
    # 1桁のSnuke数のリストは、1, 2, 3, 4, 5, 6, 7, 8, 9
    # 2桁のSnuke数のリストは、10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, ...
    # というように考えると、
    # 1桁のSnuke数のリストの各要素を10倍してくっつける
    # 2桁のSnuke数のリストの各要素を1つ前のリストの要素の1つ前にくっつける
    # 3桁のSnuke数のリストの各要素を1つ前のリストの要素の1つ前にくっつける
    # というように考えると、
    # 1桁のSnuke数のリストを作成する
    # 2桁のSnuke数のリストを作成する
    # 3桁のSnuke数のリストを作成する
    # ...
    # というように考えることができる
    #

=======

def sum_digits(n):
    """Return sum of digits in n"""
    return sum(int(d) for d in str(n))
