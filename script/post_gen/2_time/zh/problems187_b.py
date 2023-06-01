Synthesizing 10/10 solutions

=======
Suggestion 1

def sumDigits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum

a, b = map(int, input().split())
print(max(sumDigits(a), sumDigits(b)))

=======
Suggestion 2

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

=======
Suggestion 3

def S(n):
    return sum([int(i) for i in str(n)])

a, b = [int(i) for i in input().split()]
print(S(a) if S(a) > S(b) else S(b))

=======
Suggestion 4

def S(n):
    return sum(int(i) for i in str(n))

=======
Suggestion 5

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10

    return sum

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(sum(map(int, str(a))), sum(map(int, str(b)))))

=======
Suggestion 7

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num / 10)
    return sum

a, b = map(int, input().split())
print(max(sum_digits(a), sum_digits(b)))

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    a = sum(map(int, str(a)))
    b = sum(map(int, str(b)))
    print(a if a > b else b)

=======
Suggestion 9

def solution():
    a, b = map(int, input().split())
    a = sum(map(int, list(str(a))))
    b = sum(map(int, list(str(b))))
    print(max(a, b))

=======
Suggestion 10

def S(n):
    a = n//100
    b = n//10%10
    c = n%10
    return a+b+c

a,b = map(int,input().split())
print(max(S(a),S(b)))
