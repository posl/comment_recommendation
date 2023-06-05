Synthesizing 10/10 solutions

=======
Suggestion 1

def print_hex(n):
    if n < 10:
        print("0"+str(n))
    else:
        print(hex(n).upper()[2:])

=======
Suggestion 2

def hexa(n):
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
n1 = n // 16
n2 = n % 16
print(hexa(n1) + hexa(n2))

=======
Suggestion 3

def hexa(n):
    if n<10:
        return str(n)
    elif n==10:
        return 'A'
    elif n==11:
        return 'B'
    elif n==12:
        return 'C'
    elif n==13:
        return 'D'
    elif n==14:
        return 'E'
    elif n==15:
        return 'F'

=======
Suggestion 4

def main():
    n = int(input())
    print('{:02X}'.format(n))

=======
Suggestion 5

def main():
    n = int(input())
    print("%02X" % n)

main()

=======
Suggestion 6

def convert_to_hexadecimal(N):
    #将十进制转换为十六进制
    hexadecimal = hex(N)
    #将十六进制转换为大写
    hexadecimal = hexadecimal.upper()
    #去除前缀0X
    hexadecimal = hexadecimal[2:]
    #如果是一位数，则在前面加0
    if len(hexadecimal) == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal

N = int(input())
print(convert_to_hexadecimal(N))

=======
Suggestion 7

def main():
    N = int(input())
    print("%02X" % (N))

=======
Suggestion 8

def convert_to_hexadecimal(decimal):
    hexadecimal = hex(decimal)
    return hexadecimal[2:].upper()

=======
Suggestion 9

def main():
    n = int(input())
    print(format(n, '02x').upper())

=======
Suggestion 10

def hex(n):
    if n < 10:
        return n
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
    else:
        return None
