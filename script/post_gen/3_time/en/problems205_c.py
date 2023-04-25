Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
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
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
    else:
        if a > b:
            print(">")
        elif a < b:
            print("<")
        else:
            print("=")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        a = abs(a)
        b = abs(b)
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("=")
    elif c % 2 == 0:
        a = abs(a)
        b = abs(b)
        if a > b:
            print(">")
        else:
            print("<")
    elif a > b:
        print(">")
    else:
        print("<")

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
    if A >= 0 and B >= 0:
        if A > B:
            print(">")
        elif A < B:
            print("<")
        else:
            print("=")
    elif A >= 0 and B < 0:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            elif abs(A) < abs(B):
                print("<")
            else:
                print("=")
        else:
            print(">")
    elif A < 0 and B >= 0:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            elif abs(A) < abs(B):
                print("<")
            else:
                print("=")
        else:
            print("<")
    else:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print("<")
            elif abs(A) < abs(B):
                print(">")
            else:
                print("=")
        else:
            if abs(A) > abs(B):
                print(">")
            elif abs(A) < abs(B):
                print("<")
            else:
                print("=")

=======
Suggestion 6

def main():
    A,B,C = map(int,input().split())
    if A < 0 and C%2 == 0:
        A = abs(A)
    if B < 0 and C%2 == 0:
        B = abs(B)
    if A == B:
        print("=")
    elif A < B:
        print("<")
    else:
        print(">")

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if(c%2==0):
        if(abs(a)==abs(b)):
            print("=")
        elif(abs(a)>abs(b)):
            print(">")
        else:
            print("<")
    else:
        if(a==b):
            print("=")
        elif(a>b):
            print(">")
        else:
            print("<")

=======
Suggestion 8

def compare_power(a,b,c):
    if (a == b):
        return '='
    elif (c % 2 == 0):
        if (abs(a) == abs(b)):
            return '='
        elif (abs(a) < abs(b)):
            return '<'
        else:
            return '>'
    elif (c % 2 == 1):
        if (a < b):
            return '<'
        else:
            return '>'
    else:
        return 'ERROR'
