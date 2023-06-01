Synthesizing 10/10 solutions

=======
Suggestion 1

def print_4digits(num):
    if num < 10:
        print('000' + str(num))
    elif num < 100:
        print('00' + str(num))
    elif num < 1000:
        print('0' + str(num))
    else:
        print(str(num))

=======
Suggestion 2

def main():
    # 读取输入
    num = input()
    # 处理输出
    print('{:0>4}'.format(num))

=======
Suggestion 3

def main():
    n = int(input())
    if n < 10:
        print("000" + str(n))
    elif n < 100:
        print("00" + str(n))
    elif n < 1000:
        print("0" + str(n))
    else:
        print(n)

=======
Suggestion 4

def problem222_a(n):
    if n < 10:
        print('000' + str(n))
    elif n < 100:
        print('00' + str(n))
    elif n < 1000:
        print('0' + str(n))
    else:
        print(str(n))

=======
Suggestion 5

def add_zero(num):
    if num < 10:
        return '000' + str(num)
    elif num < 100:
        return '00' + str(num)
    elif num < 1000:
        return '0' + str(num)
    else:
        return str(num)

=======
Suggestion 6

def main():
    n = int(input())
    print("{:04d}".format(n))

=======
Suggestion 7

def main():
    n = int(input())
    if n < 10:
        print('000' + str(n))
    elif n < 100:
        print('00' + str(n))
    elif n < 1000:
        print('0' + str(n))
    else:
        print(n)

=======
Suggestion 8

def main():
    n = int(input())
    print('{:04d}'.format(n))

=======
Suggestion 9

def addZero(num):
    if num < 10:
        return '000' + str(num)
    elif num < 100:
        return '00' + str(num)
    elif num < 1000:
        return '0' + str(num)
    else:
        return str(num)

=======
Suggestion 10

def main():
    N = int(input())
    print('{0:04d}'.format(N))
