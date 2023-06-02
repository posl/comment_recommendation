Synthesizing 10/10 solutions

=======
Suggestion 1

def print_last_two_digits_of_number(n):
    print(str(n)[-2:])

=======
Suggestion 2

def print_last_two_digits(n):
    print(str(n)[-2:])

=======
Suggestion 3

def main():
    N = int(input())
    print(N%100)

=======
Suggestion 4

def getlast2(n):
    if n < 100 or n > 999:
        print("输入必须是3位数")
        return
    print(n % 100)

=======
Suggestion 5

def main():
    n = int(input())
    print('{0:02d}'.format(n % 100))

=======
Suggestion 6

def last_two_digit(n):
    return n % 100

=======
Suggestion 7

def problem254_a():
    N = input()
    print(N[1:3])

=======
Suggestion 8

def main():
    n = int(input())
    print(n%100)

=======
Suggestion 9

def main():
    num = int(input())
    print(num%100)

=======
Suggestion 10

def print_last_two_digits_of_n(n):
    print(n%100)
