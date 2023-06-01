Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    print('{:02X}'.format(int(input())))

=======
Suggestion 2

def hexa(n):
    if n == 0:
        return '00'
    elif n <= 9:
        return '0' + str(n)
    elif n <= 15:
        return '0' + chr(n + 55)
    elif n <= 255:
        return chr(n // 16 + 55) + chr(n % 16 + 55)

n = int(input())
print(hexa(n))

=======
Suggestion 3

def hexa(n):
    return '{:02X}'.format(n)

=======
Suggestion 4

def convert_to_hexadecimal(n):
    if n < 10:
        return str(n)
    elif 10 <= n <= 15:
        return chr(ord('A') + n - 10)
    else:
        return chr(ord('A') + n // 16 - 10) + convert_to_hexadecimal(n % 16)

=======
Suggestion 5

def main():
    n = int(input())
    print('{:02X}'.format(n))

=======
Suggestion 6

def main():
    n = int(input())
    print("{:02X}".format(n))

=======
Suggestion 7

def main():
    n = int(input())
    print(format(n, 'X').zfill(2))

=======
Suggestion 8

def main():
    N = int(input())
    print("{:02X}".format(N))

=======
Suggestion 9

def ten2hex(n):
    if n < 10:
        return str(n)
    else:
        return chr(ord('A') + n - 10)
