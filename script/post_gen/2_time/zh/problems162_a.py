Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_contain_7(num):
    if num % 10 == 7:
        return True
    else:
        return False

num = int(input())

=======
Suggestion 2

def main():
    n = input()
    if n[2] == '7':
        print('是')
    elif n[1] == '7':
        print('是')
    elif n[0] == '7':
        print('是')
    else:
        print('否')

=======
Suggestion 3

def main():
    n = int(input())
    if n % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 4

def main():
    N = int(input())
    if N % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def is_contain_7(num):
    while True:
        if num % 10 == 7:
            return True
        num = num // 10
        if num == 0:
            return False

print('是' if is_contain_7(int(input())) else '否')

=======
Suggestion 6

def solution():
    N = int(input())
    if N % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 7

def main():
    n = int(input())
    if n % 10 == 7 or n // 10 % 10 == 7 or n // 100 % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def judge(n):
    if n%10 == 7:
        return True
    elif n//10%10 == 7:
        return True
    elif n//100 == 7:
        return True
    else:
        return False

n = int(input())
