Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = input()
    sum = 0
    for c in n:
        sum += int(c)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = input()
    if sum([int(i) for i in n]) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def check_multiple_of_9(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    s = sum(n)
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    N = int(input())
    if N % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_multiple_of_9(number):
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)

    return sum_of_digits % 9 == 0

=======
Suggestion 9

def sum_of_digits(n):
    sum = 0
    while(n > 0):
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 10

def main():
    n = int(input())
    print('Yes' if n % 9 == 0 else 'No')
