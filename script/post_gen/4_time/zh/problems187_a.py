Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(sum([int(i) for i in str(a)]), sum([int(i) for i in str(b)])))

=======
Suggestion 2

def sum_digit(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

=======
Suggestion 3

def main():
    #读取输入
    line = input()
    #拆分输入
    a, b = line.split()
    #计算
    sum_a = int(a[0]) + int(a[1]) + int(a[2])
    sum_b = int(b[0]) + int(b[1]) + int(b[2])
    #比较
    if sum_a > sum_b:
        print(sum_a)
    else:
        print(sum_b)

=======
Suggestion 4

def s(n):
    return sum(map(int, str(n)))

a, b = map(int, input().split())
print(s(a) if s(a) > s(b) else s(b))

=======
Suggestion 5

def get_sum(num):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

=======
Suggestion 6

def sum_digit(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum

A, B = map(int, input().split())
print(max(sum_digit(A), sum_digit(B)))

=======
Suggestion 7

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 8

def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum

=======
Suggestion 9

def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digit(a), sum_digit(b)))

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    a_sum, b_sum = 0, 0
    while a > 0:
        a_sum += a % 10
        a //= 10
    while b > 0:
        b_sum += b % 10
        b //= 10
    print(a_sum if a_sum >= b_sum else b_sum)
