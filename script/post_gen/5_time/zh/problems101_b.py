Synthesizing 10/10 solutions

=======
Suggestion 1

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum

=======
Suggestion 2

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

N = int(input())

=======
Suggestion 3

def S(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum

n=int(input())

=======
Suggestion 4

def sumn(n):
    sum = 0
    while n > 0:
        sum += (n % 10)
        n = n // 10
    return sum

=======
Suggestion 5

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

N = int(input())

=======
Suggestion 6

def S(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

N = int(input())

=======
Suggestion 7

def getSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

=======
Suggestion 8

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 9

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 10

def getSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum
