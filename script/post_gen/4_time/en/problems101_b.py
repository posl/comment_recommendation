Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = sum(map(int, str(N)))
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def sum_of_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

n = int(input())

=======
Suggestion 3

def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

N = int(input())

=======
Suggestion 4

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

=======
Suggestion 5

def main():
    N = int(input())
    S = sum(int(c) for c in str(N))
    print("Yes" if N % S == 0 else "No")

main()

=======
Suggestion 6

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

=======
Suggestion 7

def sum_digits(n):
    return sum(int(i) for i in str(n))

=======
Suggestion 8

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

=======
Suggestion 9

def sum_of_digits(num):
    return sum([int(i) for i in str(num)])

=======
Suggestion 10

def sum_digits(num):
    # Converts integer to string, then loops through each character in the string
    # and adds it to a sum.
    num = str(num)
    sum = 0
    for c in num:
        sum += int(c)
    return sum
