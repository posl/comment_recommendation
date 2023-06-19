Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    num = int(input())
    print(num % 100)

=======
Suggestion 2

def printLastTwoDigits():
    n = int(input())
    if n < 100 or n > 999:
        print("输入错误")
    else:
        print(n % 100)

=======
Suggestion 3

def main():
    num = input()
    print(num[-2:])

=======
Suggestion 4

def print_last_two_digits(n):
    print(n%100)

=======
Suggestion 5

def main():
    n = int(input())
    print(n%100)

=======
Suggestion 6

def last_two_digits(n):
    return n % 100

print(last_two_digits(254))
print(last_two_digits(101))
print(last_two_digits(100))
print(last_two_digits(999))
print(last_two_digits(1000))

=======
Suggestion 7

def checkio(data):
    return data%100

=======
Suggestion 8

def main():
    num = input()
    if len(num) < 3:
        print('0' + num)
    else:
        print(num[-2:])

=======
Suggestion 9

def main():
    N = int(input())
    print(N%100)

=======
Suggestion 10

def last_two_digits(n):
    return n % 100

print(last_two_digits(int(input())))
