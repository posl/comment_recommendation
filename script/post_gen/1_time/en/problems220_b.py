Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    A, B = input().split()
    A = int(A, K)
    B = int(B, K)
    print(A * B)

=======
Suggestion 2

def main():
    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 3

def main():
    K = int(input())
    A, B = input().split()
    print(int(A, K) * int(B, K))

=======
Suggestion 4

def toDecimal(base, number):
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[i]) * (base ** (len(number) - i - 1))
    return decimal

=======
Suggestion 5

def base_to_decimal(base, num):
    num = str(num)
    result = 0
    for i in range(len(num)):
        result += int(num[len(num) - 1 - i]) * pow(base, i)
    return result

=======
Suggestion 6

def baseToDec (base, num):
    dec = 0
    for i in range(len(num)):
        dec += int(num[i]) * pow(base, len(num) - 1 - i)
    return dec

=======
Suggestion 7

def convertToDecimal(num, base):
    num = str(num)
    dec = 0
    for i, val in enumerate(num[::-1]):
        dec += int(val) * base ** i
    return dec

=======
Suggestion 8

def convert_to_decimal(base, number):
    # Convert a number in base to decimal
    # base: integer
    # number: string
    # return: integer
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[-i-1]) * base**i
    return decimal
