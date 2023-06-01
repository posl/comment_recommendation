Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    num = int(input())
    if num % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 2

def main():
    N = int(input())
    if N % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 3

def is_include_7(num):
    if num % 10 == 7:
        return True
    else:
        return False

=======
Suggestion 4

def is_contain_seven(n):
    if n % 10 == 7:
        return True
    elif n // 10 % 10 == 7:
        return True
    elif n // 100 % 10 == 7:
        return True
    else:
        return False

n = int(input())

=======
Suggestion 5

def is_contain_seven(num):
    return num % 10 == 7 or num // 10 % 10 == 7 or num // 100 == 7

num = int(input())
print("是" if is_contain_seven(num) else "否")

=======
Suggestion 6

def problem162_a():
    n = input()
    if '7' in n:
        print('是')
    else:
        print('否')

=======
Suggestion 7

def solution():
    n = int(input())
    if n%10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    n = int(input())
    if n % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 9

def isSevenInNum(num):
    if num%10==7:
        return True
    elif num/10%10==7:
        return True
    elif num/100%10==7:
        return True
    else:
        return False

num = int(raw_input())

=======
Suggestion 10

def main():
    # 读取输入
    n = int(input())
    # 计算
    if n % 10 == 7:
        print("是")
    else:
        print("否")
