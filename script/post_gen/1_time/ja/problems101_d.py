Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 2

def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 3

def sum_digits(n):
    """nの各桁の和を返す"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 4

def get_num(n):
    if n < 10:
        return n
    else:
        return n % 10 + get_num(n // 10)

=======
Suggestion 5

def main():
    K = int(input())
    keta = 1
    ans = []
    while len(ans) < K:
        for i in range(1, 10):
            if i * keta > 10 ** 15:
                break
            ans.append(i * keta)
        keta *= 10
    ans.sort()
    for i in range(K):
        print(ans[i])

=======
Suggestion 6

def suke(K):
    #すぬけ数のリスト
    suke_list = [1]
    #すぬけ数の最大値
    suke_max = 1
    #すぬけ数の最大値の桁数
    suke_max_d = 1
    #すぬけ数の最大値の各桁の和
    suke_max_d_sum = 1
    #すぬけ数の最大値の各桁の和の桁数
    suke_max_d_sum_d = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値
    suke_max_d_sum_d_max = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値の最大値
    suke_max_d_sum_d_max_max = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値の最大値の最大値
    suke_max_d_sum_d_max_max_max = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値の最大値の最大値の最大値
    suke_max_d_sum_d_max_max_max_max = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値の最大値の最大値の最大値の最大値
    suke_max_d_sum_d_max_max_max_max_max = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値の最大値の最大値の最大値の最大値の最大値
    suke_max_d_sum_d_max_max_max_max_max_max = 1
    #すぬけ数の最大値の各桁の和の桁数の最大値の

=======
Suggestion 7

def sum_digits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 8

def main():
    K = int(input())
    suke = [1]
    for i in range(2, 10**15):
        if i % 10 == 0:
            continue
        if i % sum(int(n) for n in str(i)) == 0:
            suke.append(i)
        if len(suke) == K:
            break
    for i in range(K):
        print(suke[i])

=======
Suggestion 9

def f(n):
    return n / sum(int(i) for i in str(n))

=======
Suggestion 10

def sum_of_digits(n):
    return sum(map(int, str(n)))
