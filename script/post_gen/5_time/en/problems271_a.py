Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print('{:02X}'.format(n))

=======
Suggestion 2

def main():
    n = int(input())
    print('{:02x}'.format(n))

=======
Suggestion 3

def main():
    N = int(input())
    print('{:02X}'.format(N))

=======
Suggestion 4

def main():
    n = int(input())
    print("%02X" % n)

=======
Suggestion 5

def convert_to_hexadecimal(num):
    return hex(num).upper()[2:].zfill(2)

print(convert_to_hexadecimal(int(input())))

=======
Suggestion 6

def main():
    print('{:02X}'.format(int(input())))

=======
Suggestion 7

def main():
	print(hex(int(input()))[2:].upper().zfill(2))
