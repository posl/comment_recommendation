Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N < 16:
        print('0' + hex(N)[2:].upper())
    else:
        print(hex(N)[2:].upper())

=======
Suggestion 2

def hexa (n):
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

=======
Suggestion 3

def main():
    N = int(input())
    print("{0:02X}".format(N))

=======
Suggestion 4

def main():
    N = int(input())
    print("{:02X}".format(N))

=======
Suggestion 5

def main():
    n = int(input())
    print("{0:02X}".format(n))

=======
Suggestion 6

def main():
    N = int(input())
    #print(N)
    hex = str(hex(N))
    #print(hex)
    hex = hex[2:]
    #print(hex)
    if len(hex) == 1:
        hex = '0' + hex
    print(hex)

=======
Suggestion 7

def main():
    N = int(input())
    print(f"{N:02X}")

=======
Suggestion 8

def main():
    N = int(input())
    print(format(N, "02X"))
