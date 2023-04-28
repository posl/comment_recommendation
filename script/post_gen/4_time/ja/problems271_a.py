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
    else:
        return ''

=======
Suggestion 2

def main():
    n = int(input())
    print('{:02X}'.format(n))

=======
Suggestion 3

def main():
    n = int(input())
    print("{:02X}".format(n))

=======
Suggestion 4

def main():
    n = int(input())
    print('%02X' % n)

=======
Suggestion 5

def main():
    N = int(input())
    print('{:02x}'.format(N))

=======
Suggestion 6

def main():
    print('{:02X}'.format(int(input())))
