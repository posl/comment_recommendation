Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def print_4_digit_number(number):
    if number < 10:
        print("000" + str(number))
    elif number < 100:
        print("00" + str(number))
    elif number < 1000:
        print("0" + str(number))
    else:
        print(str(number))

=======
Suggestion 2

def main():
    n = int(input())
    print("{:04d}".format(n))

=======
Suggestion 3

def main():
    n = input()
    print(n.zfill(4))

=======
Suggestion 4

def main():
    n = int(input())
    print("{0:04d}".format(n))

=======
Suggestion 5

def main():
    N = int(input())
    if N < 10:
        print("000" + str(N))
    elif N < 100:
        print("00" + str(N))
    elif N < 1000:
        print("0" + str(N))
    else:
        print(str(N))

=======
Suggestion 6

def add_zero(n):
    if n < 0 or n > 9999:
        print("输入的数字超出范围")
    else:
        if n < 10:
            print("000" + str(n))
        elif n < 100:
            print("00" + str(n))
        elif n < 1000:
            print("0" + str(n))
        else:
            print(n)

add_zero(1)
add_zero(11)
add_zero(111)
add_zero(1111)
add_zero(11111)
add_zero(111111)
add_zero(1111111)

=======
Suggestion 7

def main():
    n = int(input())
    print('{:0>4}'.format(n))

=======
Suggestion 8

def solve():
    n = int(input())
    if n < 10:
        print('000'+str(n))
    elif n < 100:
        print('00'+str(n))
    elif n < 1000:
        print('0'+str(n))
    else:
        print(str(n))
