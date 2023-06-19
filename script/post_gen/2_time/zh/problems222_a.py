Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    print(input().zfill(4))

=======
Suggestion 2

def main():
    N = int(input())
    if N < 10:
        print("000" + str(N))
    elif N < 100:
        print("00" + str(N))
    elif N < 1000:
        print("0" + str(N))
    else:
        print(N)
main()

=======
Suggestion 3

def add_zero(num):
    num_str = str(num)
    while len(num_str) < 4:
        num_str = '0' + num_str
    return num_str

=======
Suggestion 4

def main():
    n = int(input())
    print('{:0>4d}'.format(n))

=======
Suggestion 5

def main():
    num = input()
    print('{:0=4}'.format(num))

=======
Suggestion 6

def add_zero(number):
    if number > 9999 or number < 0:
        return "ERROR"
    else:
        return "{:04d}".format(number)

print(add_zero(int(input())))

=======
Suggestion 7

def main():
    n = int(input())
    print('{:04d}'.format(n))

=======
Suggestion 8

def addZero(n):
    n = str(n)
    while len(n) < 4:
        n = '0' + n
    return n

=======
Suggestion 9

def main():
    n = int(input())
    print("{:04d}".format(n))
