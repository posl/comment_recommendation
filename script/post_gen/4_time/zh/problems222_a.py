Synthesizing 10/10 solutions

=======
Suggestion 1

def problem222_a(n):
    if n < 0 or n > 9999:
        print('error')
        return
    print('{:0>4d}'.format(n))

problem222_a(321)
problem222_a(7777)
problem222_a(1)
problem222_a(10000)
problem222_a(-1)

=======
Suggestion 2

def main():
    n = int(input())
    print("%04d" % n)

=======
Suggestion 3

def main():
    N = input()
    print(N.zfill(4))

=======
Suggestion 4

def main():
    num = int(input())
    print("{:04d}".format(num))

=======
Suggestion 5

def main():
    n = int(input())
    print('{:04d}'.format(n))

=======
Suggestion 6

def add_zero(num):
    num_str = str(num)
    while(len(num_str) < 4):
        num_str = '0' + num_str
    return num_str

=======
Suggestion 7

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
Suggestion 8

def addZero(n):
    if n < 10:
        return "000" + str(n)
    elif n < 100:
        return "00" + str(n)
    elif n < 1000:
        return "0" + str(n)
    else:
        return str(n)

=======
Suggestion 9

def print_four_digits(num):
    print('{:04}'.format(num))

=======
Suggestion 10

def add_zero(num):
    if num < 10:
        return "000" + str(num)
    elif num < 100:
        return "00" + str(num)
    elif num < 1000:
        return "0" + str(num)
    else:
        return str(num)
