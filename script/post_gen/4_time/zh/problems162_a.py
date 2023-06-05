Synthesizing 10/10 solutions

=======
Suggestion 1

def judge():
    number = int(input())
    if number%10 == 7 or (number//10)%10 == 7 or (number//100)%10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 2

def isContainSeven(num):
    if num % 10 == 7:
        return True
    elif num // 10 % 10 == 7:
        return True
    elif num // 100 % 10 == 7:
        return True
    else:
        return False

=======
Suggestion 3

def is_7(n):
    if n % 10 == 7:
        return True
    elif n // 10 == 0:
        return False
    else:
        return is_7(n // 10)

n = int(input())

=======
Suggestion 4

def main():
    n = int(input())
    if n % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def isSeven(number):
    if number % 10 == 7:
        return True
    elif number / 10 == 7:
        return True
    elif number / 100 == 7:
        return True
    else:
        return False

=======
Suggestion 6

def isIncludeSeven(num):
    numStr = str(num)
    for i in numStr:
        if i == '7':
            return True
    return False

=======
Suggestion 7

def main():
    num = int(input())
    if num % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def has_seven(n):
    while n > 0:
        if n % 10 == 7:
            return True
        n //= 10
    return False

=======
Suggestion 9

def is_contain_seven(x):
    return x % 10 == 7 or x // 10 % 10 == 7 or x // 100 % 10 == 7

=======
Suggestion 10

def main():
    N = int(input())
    if N % 10 == 7:
        print("是")
    else:
        print("否")
