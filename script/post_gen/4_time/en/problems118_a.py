Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if b%a == 0:
        print(a+b)
    else:
        print(b-a)
    return

=======
Suggestion 4

def is_divisor(a, b):
    return b % a == 0
