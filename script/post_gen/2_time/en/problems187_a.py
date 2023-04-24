Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_digits(n):
    return sum(int(d) for d in str(n))

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 2

def sum_digits(num):
    return sum([int(x) for x in str(num)])

A, B = [int(x) for x in input().split()]
print(max(sum_digits(A), sum_digits(B)))

=======
Suggestion 3

def sum_digits(n):
    return sum([int(i) for i in str(n)])

A, B = map(int, input().split())
print(max(sum_digits(A), sum_digits(B)))

A, B = map(int, input().split())

=======
Suggestion 4

def sum_digits(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

=======
Suggestion 5

def sumDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumDigits(n // 10)

=======
Suggestion 6

def sum_of_digits(x):
    return sum(int(d) for d in str(x))

a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

=======
Suggestion 7

def sum_digits(n):
    return sum(int(c) for c in str(n))

a, b = map(int, input().split())
a = sum_digits(a)
b = sum_digits(b)
print(a if a >= b else b)

=======
Suggestion 8

def sum_digits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 9

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 10

def sum_of_digits(n):
    return sum(map(int, str(n)))
