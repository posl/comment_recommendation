Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = sum(map(int, str(N)))
    if N % S == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 3

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

=======
Suggestion 4

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

n = int(input())

=======
Suggestion 5

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

n = int(input())

=======
Suggestion 6

def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 7

def sum_digits(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

=======
Suggestion 8

def S(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum

n = int(input())

=======
Suggestion 9

def sum_digits(n):
    return sum(int(i) for i in str(n))
