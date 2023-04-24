Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A**C > B**C:
        print(">")
    elif A**C < B**C:
        print("<")
    else:
        print("=")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a**c > b**c:
        print(">")
    elif a**c < b**c:
        print("<")
    else:
        print("=")

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    if A**C > B**C:
        print('>')
    elif A**C < B**C:
        print('<')
    else:
        print('=')

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if A == B:
        print('=')
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if abs(A) < abs(B):
                print('>')
            else:
                print('<')
        else:
            if A < B:
                print('>')
            else:
                print('<')
    elif A < 0:
        if C % 2 == 0:
            if abs(A) < B:
                print('>')
            else:
                print('<')
        else:
            print('<')
    elif B < 0:
        if C % 2 == 0:
            if A < abs(B):
                print('>')
            else:
                print('<')
        else:
            print('>')
    else:
        if A < B:
            print('<')
        else:
            print('>')

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    pow_A = A ** C
    pow_B = B ** C
    if pow_A > pow_B:
        print(">")
    elif pow_A == pow_B:
        print("=")
    else:
        print("<")

=======
Suggestion 6

def main():
    A,B,C = map(int,input().split())
    if A<0 and B<0:
        if C%2==0:
            if A<B:
                print(">")
            elif A>B:
                print("<")
            else:
                print("=")
        else:
            if A<B:
                print("<")
            elif A>B:
                print(">")
            else:
                print("=")
    elif A<0 and B>=0:
        if C%2==0:
            print(">")
        else:
            if A<B:
                print("<")
            elif A>B:
                print(">")
            else:
                print("=")
    elif A>=0 and B<0:
        if C%2==0:
            print("<")
        else:
            if A<B:
                print("<")
            elif A>B:
                print(">")
            else:
                print("=")
    else:
        if A<B:
            print("<")
        elif A>B:
            print(">")
        else:
            print("=")

=======
Suggestion 7

def main():
    A,B,C = map(int,input().split())
    #print(A,B,C)
    if A > 0 and B > 0:
        if A > B:
            print(">")
        elif A < B:
            print("<")
        else:
            print("=")
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            elif abs(A) < abs(B):
                print("<")
            else:
                print("=")
        else:
            if A > B:
                print(">")
            elif A < B:
                print("<")
            else:
                print("=")
    else:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            elif abs(A) < abs(B):
                print("<")
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
Suggestion 8

def pow(a,b,c):
    if a<0 and b>0:
        if c%2==0:
            return '>'
        else:
            return '<'
    elif a<0 and b<0:
        if c%2==0:
            return '='
        else:
            return '<'
    elif a>0 and b<0:
        if c%2==0:
            return '='
        else:
            return '>'
    elif a==0 and b==0:
        return '='
    elif a==0:
        return '<'
    elif b==0:
        return '>'
    elif a>0 and b>0:
        return '>'

a,b,c = map(int,input().split())
print(pow(a,b,c))
