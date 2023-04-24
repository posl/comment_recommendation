Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if pow(A, C) > pow(B, C):
        print(">")
    elif pow(A, C) < pow(B, C):
        print("<")
    else:
        print("=")

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if A**C < B**C:
        print("<")
    elif A**C > B**C:
        print(">")
    else:
        print("=")

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if A**C > B**C:
        print(">")
    elif A**C < B**C:
        print("<")
    else:
        print("=")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a < 0 and b > 0 and c % 2 == 1:
        print('>')
    elif a < 0 and b > 0 and c % 2 == 0:
        if abs(a) > b:
            print('>')
        elif abs(a) < b:
            print('<')
        else:
            print('=')
    elif a < 0 and b < 0:
        if abs(a) > abs(b):
            print('>')
        elif abs(a) < abs(b):
            print('<')
        else:
            print('=')
    else:
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    if a > 0 and b > 0:
        if a < b:
            print("<")
        elif a > b:
            print(">")
        else:
            print("=")
    elif a < 0 and b < 0:
        if a < b:
            print(">")
        elif a > b:
            print("<")
        else:
            print("=")
    elif a < 0 and b > 0:
        if c % 2 == 0:
            if abs(a) < b:
                print("<")
            elif abs(a) > b:
                print(">")
            else:
                print("=")
        else:
            print("<")
    else:
        if c % 2 == 0:
            if a < abs(b):
                print("<")
            elif a > abs(b):
                print(">")
            else:
                print("=")
        else:
            print(">")

=======
Suggestion 6

def main():
    A, B, C = [int(x) for x in input().split()]
    if A == B:
        print("=")
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if A < B:
                print(">")
            else:
                print("<")
        else:
            if A < B:
                print("<")
            else:
                print(">")
    elif A < 0:
        if C % 2 == 0:
            if A < B:
                print(">")
            else:
                print("<")
        else:
            print("<")
    elif B < 0:
        if C % 2 == 0:
            if A < B:
                print(">")
            else:
                print("<")
        else:
            print(">")
    else:
        if A < B:
            print("<")
        else:
            print(">")

=======
Suggestion 7

def compare_power(A, B, C):
    if A < 0 and B < 0:
        if C % 2 == 0:
            if A > B:
                return '>'
            elif A < B:
                return '<'
            else:
                return '='
        else:
            if A > B:
                return '<'
            elif A < B:
                return '>'
            else:
                return '='
    elif A < 0 or B < 0:
        if C % 2 == 0:
            if A > B:
                return '>'
            elif A < B:
                return '<'
            else:
                return '='
        else:
            if A > B:
                return '>'
            elif A < B:
                return '<'
            else:
                return '='
    else:
        if A > B:
            return '>'
        elif A < B:
            return '<'
        else:
            return '='

=======
Suggestion 8

def main():
    # Read the input
    A, B, C = map(int, input().split())

    # Display the result
    if pow(A, C) > pow(B, C):
        print(">")
    elif pow(A, C) < pow(B, C):
        print("<")
    else:
        print("=")
