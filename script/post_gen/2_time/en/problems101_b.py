Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = sum(map(int, str(N)))
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def sumDigits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

n = int(input())

=======
Suggestion 3

def sum_digits(n):
    return sum(int(i) for i in str(n))

n = int(input())

=======
Suggestion 4

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

=======
Suggestion 5

def sum_of_digits(n):
    return sum([int(d) for d in str(n)])

=======
Suggestion 6

def sumOfDigits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 7

def sumDigits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 8

def sumOfDigits(n):
    return sum(int(digit) for digit in str(n))

=======
Suggestion 9

def sum_digits(n):
    return sum(int(i) for i in str(n))

n = int(input())
print("Yes" if n % sum_digits(n) == 0 else "No")

This is a very short solution, but it is not very efficient. It is O(n) in time and O(1) in space.
