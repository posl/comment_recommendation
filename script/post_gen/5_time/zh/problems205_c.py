Synthesizing 10/10 solutions

=======
Suggestion 1

def compare_pow(a,b,c):
    if pow(a,c) < pow(b,c):
        return '<'
    elif pow(a,c) > pow(b,c):
        return '>'
    else:
        return '='

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if pow(a,c)<pow(b,c):
        print('<')
    elif pow(a,c)>pow(b,c):
        print('>')
    else:
        print('=')

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    if a == b:
        print("=")
    elif a > 0 and b > 0:
        if a > b:
            print(">")
        else:
            print("<")
    elif a > 0 and b < 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                print(">")
            else:
                print("<")
        else:
            print(">")
    elif a < 0 and b > 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                print(">")
            else:
                print("<")
        else:
            print("<")
    elif a < 0 and b < 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                print(">")
            else:
                print("<")
        else:
            if abs(a) > abs(b):
                print("<")
            else:
                print(">")

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if A == B:
        print("=")
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            else:
                print("<")
        else:
            if abs(A) > abs(B):
                print("<")
            else:
                print(">")
    elif A < 0 and B > 0:
        if C % 2 == 0:
            if abs(A) > B:
                print(">")
            else:
                print("<")
        else:
            print("<")
    elif A > 0 and B < 0:
        if C % 2 == 0:
            if A > abs(B):
                print(">")
            else:
                print("<")
        else:
            print(">")
    elif A > 0 and B > 0:
        if C % 2 == 0:
            if A > B:
                print(">")
            else:
                print("<")
        else:
            if A > B:
                print(">")
            else:
                print("<")
    else:
        print("error")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if pow(a, c) < pow(b, c):
        print("<")
    elif pow(a, c) > pow(b, c):
        print(">")
    else:
        print("=")

=======
Suggestion 6

def pow(a,b):
    if b == 0:
        return 1
    return a * pow(a,b-1)

=======
Suggestion 7

def compare_pow(a, b, c):
    if a == b:
        return '='
    elif c % 2 == 0:
        return '>' if abs(a) > abs(b) else '<'
    elif c % 2 == 1:
        return '>' if a > b else '<'

=======
Suggestion 8

def compare(a, b):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "="

a, b, c = map(int, input().split())
print(compare(pow(a, c), pow(b, c)))

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a > 0 and b > 0:
        if a > b:
            print('>')
        elif a == b:
            print('=')
        else:
            print('<')
    elif a < 0 and b < 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                print('>')
            elif abs(a) == abs(b):
                print('=')
            else:
                print('<')
        else:
            if abs(a) > abs(b):
                print('<')
            elif abs(a) == abs(b):
                print('=')
            else:
                print('>')
    elif a < 0 and b > 0:
        if c % 2 == 0:
            if abs(a) > b:
                print('>')
            elif abs(a) == b:
                print('=')
            else:
                print('<')
        else:
            print('<')
    else:
        if c % 2 == 0:
            if a > abs(b):
                print('>')
            elif a == abs(b):
                print('=')
            else:
                print('<')
        else:
            print('>')

=======
Suggestion 10

def main():
    A,B,C = map(int, input().split())
    if A == B:
        print("=")
    elif C % 2 == 0:
        A = abs(A)
        B = abs(B)
        if A > B:
            print(">")
        else:
            print("<")
    elif C % 2 != 0:
        if A > B:
            print(">")
        else:
            print("<")
