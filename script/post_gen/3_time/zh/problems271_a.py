Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print('{:02x}'.format(n))

=======
Suggestion 2

def main():
    n = int(input())
    if n < 16:
        print("0" + hex(n)[2:].upper())
    else:
        print(hex(n)[2:].upper())

=======
Suggestion 3

def main():
    n = int(input())
    print('{:02X}'.format(n))

=======
Suggestion 4

def main():
    n = int(input())
    print("%02X" % n)

=======
Suggestion 5

def toHexadecimal(N):
    if N < 10:
        return N
    elif N == 10:
        return 'A'
    elif N == 11:
        return 'B'
    elif N == 12:
        return 'C'
    elif N == 13:
        return 'D'
    elif N == 14:
        return 'E'
    elif N == 15:
        return 'F'
    else:
        return 0

N = int(input())
print(toHexadecimal(N // 16), end='')
print(toHexadecimal(N % 16))

=======
Suggestion 6

def convert_to_hex(num):
    hex_num = hex(num)
    return hex_num[2:].upper().zfill(2)

=======
Suggestion 7

def problem271_a():
    n = int(input())
    print('{:02X}'.format(n)) # X大写表示16进制，x小写表示16进制
    # print(format(n,'02X'))

=======
Suggestion 8

def main():
    n = int(input())
    if n < 16:
        print('0' + hex(n)[2:])
    else:
        print(hex(n)[2:])

=======
Suggestion 9

def hexa(n):
    a = n // 16
    b = n % 16
    if a < 10:
        a = str(a)
    elif a == 10:
        a = 'A'
    elif a == 11:
        a = 'B'
    elif a == 12:
        a = 'C'
    elif a == 13:
        a = 'D'
    elif a == 14:
        a = 'E'
    else:
        a = 'F'
    if b < 10:
        b = str(b)
    elif b == 10:
        b = 'A'
    elif b == 11:
        b = 'B'
    elif b == 12:
        b = 'C'
    elif b == 13:
        b = 'D'
    elif b == 14:
        b = 'E'
    else:
        b = 'F'
    return a+b

n = int(input())
print(hexa(n))
