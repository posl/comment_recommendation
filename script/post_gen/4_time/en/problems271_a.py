Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def convert_to_hex(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'

n = int(input())
first_digit = n // 16
second_digit = n % 16
print(convert_to_hex(first_digit) + convert_to_hex(second_digit))

=======
Suggestion 2

def main():
    n = int(input())
    print('{:02X}'.format(n))

=======
Suggestion 3

def main():
    n = int(input())
    print('{:02x}'.format(n))

=======
Suggestion 4

def convert_to_hexa(num):
    if num <= 15:
        return "0"+hex(num).replace("0x", "").upper()
    else:
        return hex(num).replace("0x", "").upper()

=======
Suggestion 5

def main():
    n = int(input())
    print("{:02x}".format(n))

=======
Suggestion 6

def main():
    N = int(input())
    print('{:02x}'.format(N))

=======
Suggestion 7

def main():
    n = int(input())
    print('%02x' % n)

=======
Suggestion 8

def main():
    N = int(input())
    print(format(N, '02x'))

=======
Suggestion 9

def main():
    print('{:02X}'.format(int(input())))
