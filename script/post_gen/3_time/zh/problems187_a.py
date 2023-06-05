Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def getSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

a, b = map(int, input().split())
print(max(getSum(a), getSum(b)))

=======
Suggestion 2

def S(n):
    return int(n[0]) + int(n[1]) + int(n[2])

a, b = input().split()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    a1 = a // 100
    a2 = a % 100 // 10
    a3 = a % 10
    b1 = b // 100
    b2 = b % 100 // 10
    b3 = b % 10
    print(max(a1+a2+a3, b1+b2+b3))

=======
Suggestion 4

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 5

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

a, b = map(int, input().split())
print(max(sum_of_digits(a), sum_of_digits(b)))

=======
Suggestion 6

def sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

=======
Suggestion 7

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum
