Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    a, b = map(int, input().split())
    print(a*b)

=======
Suggestion 2

def main():
    k = int(input())
    a, b = map(str, input().split())
    a = int(a, k)
    b = int(b, k)
    print(a * b)

=======
Suggestion 3

def main():
    K = int(input())
    A,B = map(int,input().split())
    print(A*B)

=======
Suggestion 4

def main():
    K = int(input())
    A, B = map(str, input().split())
    A = int(A, K)
    B = int(B, K)
    print(A*B)

=======
Suggestion 5

def main():
    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a*b)

=======
Suggestion 6

def base10toN(num, base):
    """Change decimal `num` to `base` numeral system.
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string
