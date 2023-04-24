Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

n = int(input())

=======
Suggestion 2

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

N = int(input())

=======
Suggestion 3

def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

n = int(input())
print("Yes" if n % digit_sum(n) == 0 else "No")

=======
Suggestion 5

def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

N = int(input())

=======
Suggestion 6

def sum_of_digits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

n = int(input())
print("Yes" if n % sum_of_digits(n) == 0 else "No")

=======
Suggestion 7

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

n = int(input())
print("Yes" if n % sum_of_digits(n) == 0 else "No")

=======
Suggestion 8

def main():
    n = int(input())
    s = sum(list(map(int, list(str(n)))))
    if n%s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def problems101_b():
    n = int(input())
    s = sum([int(x) for x in list(str(n))])
    if n%s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def SumOfDigits(n):
    return sum(int(c) for c in str(n))

n = int(input())
