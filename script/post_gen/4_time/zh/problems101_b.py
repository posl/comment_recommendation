Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem101_b(N):
    if N < 1 or N > 10**9:
        return "No"
    sum = 0
    num = N
    while num > 0:
        sum += num % 10
        num //= 10
    if sum % N == 0:
        return "Yes"
    else:
        return "No"

=======
Suggestion 2

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 3

def s(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 4

def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

n = int(input())

=======
Suggestion 5

def S(n):
    result = 0
    while n > 0:
        result += n%10
        n //= 10
    return result

n = int(input())

=======
Suggestion 6

def check(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    if(n%sum==0):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

N = int(input())

=======
Suggestion 8

def S(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

N = int(input())

=======
Suggestion 9

def sumDigits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum
