Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def print_last_two_digits(N):
    print(N % 100)

=======
Suggestion 2

def main():
    n = int(input())
    print(n % 100)

=======
Suggestion 3

def print_last_two_digits(num):
    if num > 99 and num < 1000:
        print(str(num)[-2:])
    else:
        print('error')

=======
Suggestion 4

def print_last_two_digits():
    num = int(input())
    print(num % 100)

=======
Suggestion 5

def get_last_two_digits(n):
    return n % 100

=======
Suggestion 6

def main():
    N = int(input())
    print(N%100)

=======
Suggestion 7

def main():
    x = input()
    print(x[1:])

=======
Suggestion 8

def print_last_two_digits(n):
    if n < 100 or n > 999:
        return
    print(n % 100)
