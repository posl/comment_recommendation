Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

=======
Suggestion 2

def main():
    n = int(input())
    s = sum(int(i) for i in str(n))
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    if n % sum([int(i) for i in str(n)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def S(n):
    return sum(map(int, str(n)))

n = int(input())
print('Yes' if n % S(n) == 0 else 'No')

=======
Suggestion 5

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum

=======
Suggestion 6

def s(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum

=======
Suggestion 7

def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if S % N == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def S(n):
    s = 0
    while n > 0:
        s += n%10
        n = n//10
    return s

=======
Suggestion 9

def check_divisible(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    if number % sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def getSum(n):
    sum = 0
    while n > 0:
        sum = sum + n%10
        n = n // 10
    return sum

n = int(input())
