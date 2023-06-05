Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_seven(n):
    if "7" in str(n):
        return True
    else:
        return False

n = int(input())

=======
Suggestion 2

def main():
    a = input()
    if '7' in a:
        print('是')
    else:
        print('否')

=======
Suggestion 3

def main():
    N = int(input())
    if N % 10 == 7:
        print("是")
    else:
        print("否")

=======
Suggestion 4

def seven_check(number):
    if '7' in str(number):
        return '是'
    else:
        return '否'

=======
Suggestion 5

def is_contain_seven(n):
    if n % 10 == 7:
        return True
    elif n // 10 == 7:
        return True
    elif n // 100 == 7:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    #输入
    N = int(input())
    #处理
    if N % 10 == 7:
        print('是')
    else:
        print('否')
    #输出

=======
Suggestion 7

def is_seven_included(num):
    num_str = str(num)
    return '7' in num_str

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

def isSeven(n):
    for i in str(n):
        if i == "7":
            return True
    return False
