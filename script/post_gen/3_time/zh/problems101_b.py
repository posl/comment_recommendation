Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    sum = 0
    for i in str(N):
        sum += int(i)
    if N % sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 3

def sum_digit(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res

=======
Suggestion 4

def s(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

n = int(input())

=======
Suggestion 5

def sumN(n):
    s = 0
    while n>0:
        s+=n%10
        n//=10
    return s

=======
Suggestion 6

def S(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s

N=int(input())
print('Yes' if N%S(N)==0 else 'No')

=======
Suggestion 7

def S(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

=======
Suggestion 8

def problem101_b():
    n = int(input())
    sum = 0
    for i in str(n):
        sum += int(i)
    if n % sum == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def check(n):
    s = 0
    for i in str(n):
        s += int(i)
    return n % s == 0

n = int(input())
print("Yes" if check(n) else "No")

=======
Suggestion 10

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

N = int(input())
s = sum_digits(N)
