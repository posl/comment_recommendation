Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(A)
    elif A == B:
        print(A)
    else:
        print(3 - A - B)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
    else:
        print(3 - a - b)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(3 - A - B)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(2*b-a)

=======
Suggestion 5

def problem270_a(a,b):
    c = 0
    if a > 0 and b > 0:
        c = 3 - a - b
    elif a > 0 and b == 0:
        c = 3 - a
    elif a == 0 and b > 0:
        c = 3 - b
    return c

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(3 - a - b + a * b)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    print(3-a-b)

=======
Suggestion 8

def solve():
    a,b = map(int,input().split())
    print(3-a-b)

=======
Suggestion 9

def solve():
    a, b = map(int, input().split())
    print((a & b) + (a ^ b))
