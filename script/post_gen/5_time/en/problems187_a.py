Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 2

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(sum([int(i) for i in str(a)]), sum([int(i) for i in str(b)])))

=======
Suggestion 4

def sum_digits(num):
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    return sum

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 5

def sum_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum

A, B = map(int, input().split())

=======
Suggestion 6

def sum_digits(number):
    return sum(int(digit) for digit in str(number))

a, b = map(int, input().split())
