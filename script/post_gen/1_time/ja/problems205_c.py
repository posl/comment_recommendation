Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a**c < b**c:
        print("<")
    elif a**c > b**c:
        print(">")
    else:
        print("=")

=======
Suggestion 2

def main():
    A,B,C = map(int,input().split())
    if A**C > B**C:
        print(">")
    elif A**C < B**C:
        print("<")
    else:
        print("=")

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    if a**c > b**c:
        print('>')
    elif a**c < b**c:
        print('<')
    else:
        print('=')

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a ** c == b ** c:
        print("=")
    elif a ** c > b ** c:
        print(">")
    else:
        print("<")

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
    if A > 0 and B > 0:
        if A > B:
            print(">")
        elif A < B:
            print("<")
        else:
            print("=")
    elif A < 0 and B < 0:
        if A > B:
            print("<")
        elif A < B:
            print(">")
        else:
            print("=")
    else:
        if A > B:
            print(">")
        elif A < B:
            print("<")
        else:
            print("=")

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    if A < 0 and B > 0:
        if C % 2 == 0:
            if A ** C > B ** C:
                print(">")
            elif A ** C < B ** C:
                print("<")
            else:
                print("=")
        else:
            if A ** C > B ** C:
                print("<")
            elif A ** C < B ** C:
                print(">")
            else:
                print("=")
    else:
        if A ** C > B ** C:
            print(">")
        elif A ** C < B ** C:
            print("<")
        else:
            print("=")

=======
Suggestion 7

def main():
    A,B,C=map(int,input().split())
    if A<0 and C%2==1:
        if A**C > B**C:
            print(">")
        elif A**C < B**C:
            print("<")
        else:
            print("=")
    else:
        if A**C > B**C:
            print(">")
        elif A**C < B**C:
            print("<")
        else:
            print("=")

=======
Suggestion 8

def pow(a,b):
    if b == 1:
        return a
    else:
        return a*pow(a,b-1)

A,B,C = map(int,input().split())
