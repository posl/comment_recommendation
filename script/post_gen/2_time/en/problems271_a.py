Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print("{0:02X}".format(N))

=======
Suggestion 2

def main():
    n = int(input())
    print("{:02X}".format(n))

=======
Suggestion 3

def convertToHex(n):
    if n < 16:
        return "0" + hex(n)[2:].upper()
    else:
        return hex(n)[2:].upper()

=======
Suggestion 4

def main():
    n = int(input())
    print("{0:02X}".format(n))

main()

=======
Suggestion 5

def main():
    N = int(input())
    print(format(N, '02X'))

=======
Suggestion 6

def main():
    N = int(input())
    print('%02X' % N)
