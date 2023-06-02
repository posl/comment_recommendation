Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def S(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 2

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 3

def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digit(a), sum_digit(b)))

=======
Suggestion 4

def sum_of_digits(num):
    sum = 0
    while (num > 0):
        sum += num % 10
        num = num // 10
    return sum

=======
Suggestion 5

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(sum_digits(a) if sum_digits(a) > sum_digits(b) else sum_digits(b))
# print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 6

def getSum(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = int(n/10)
    return sum

=======
Suggestion 7

def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n /= 10
    return sum

a, b = map(int, raw_input().split())
print max(sum_of_digits(a), sum_of_digits(b))

=======
Suggestion 8

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

=======
Suggestion 9

def S(n):
    n_str = str(n)
    sum = 0
    for i in n_str:
        sum += int(i)
    return sum

a, b = input().split()
a = int(a)
b = int(b)
print(max(S(a), S(b)))
