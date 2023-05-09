Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if C % 2 == 0:
        if abs(A) > abs(B):
            print('>')
        elif abs(A) < abs(B):
            print('<')
        else:
            print('=')
    else:
        if A > B:
            print('>')
        elif A < B:
            print('<')
        else:
            print('=')

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if C % 2 == 0:
        A = abs(A)
        B = abs(B)
    if A == B:
        print("=")
    elif A > B:
        print(">")
    else:
        print("<")

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if C%2 == 0:
        A = abs(A)
        B = abs(B)
    if A == B:
        print('=')
    elif A > B:
        print('>')
    else:
        print('<')

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    if c%2 == 0:
        a = abs(a)
        b = abs(b)
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if c%2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print('=')
    elif a > b:
        print('>')
    else:
        print('<')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a < 0 and b < 0 and c % 2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print('=')
    elif a < b:
        print('<')
    else:
        print('>')

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if (c%2 == 0):
        if (abs(a) > abs(b)):
            print(">")
        elif (abs(a) < abs(b)):
            print("<")
        else:
            print("=")
    else:
        if (a > b):
            print(">")
        elif (a < b):
            print("<")
        else:
            print("=")

=======
Suggestion 8

def solve(A,B,C):
    if C%2==0:
        A=abs(A)
        B=abs(B)
    if A==B:
        print("=")
    elif A>B:
        print(">")
    else:
        print("<")
    return 0

=======
Suggestion 9

def pow(a, b):
    if a >= 0:
        return a**b
    else:
        if b % 2 == 0:
            return (-a)**b
        else:
            return -((-a)**b)

A, B, C = map(int, input().split())
