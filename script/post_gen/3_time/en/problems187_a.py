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

def sum_of_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    sum_a = sum(map(int, str(a)))
    sum_b = sum(map(int, str(b)))
    print(max(sum_a, sum_b))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 6

def getSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num / 10)
    return sum

=======
Suggestion 7

def sum_digits(num):
    return sum(int(x) for x in str(num))
