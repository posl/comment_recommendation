Synthesizing 10/10 solutions

=======
Suggestion 1

def pow(a, b):
    if a < 0 and b % 2 == 0:
        return -a**b
    else:
        return a**b

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    if pow(a,c) < pow(b,c):
        print('<')
    elif pow(a,c) > pow(b,c):
        print('>')
    else:
        print('=')

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if pow(a,c) < pow(b,c):
        print("<")
    elif pow(a,c) > pow(b,c):
        print(">")
    else:
        print("=")

=======
Suggestion 4

def pow(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result

a,b,c = map(int,input().split())

=======
Suggestion 5

def pow(a,b):
    if a==0:
        return 0
    if b==0:
        return 1
    if b==1:
        return a
    if b<0:
        return 1/pow(a,-b)
    if b%2==0:
        return pow(a,b/2)*pow(a,b/2)
    else:
        return pow(a,(b-1)/2)*pow(a,(b-1)/2)*a

=======
Suggestion 6

def main():
    # 读取输入
    A, B, C = map(int, input().split())

    # 求解并输出
    if pow(A, C) > pow(B, C):
        print(">")
    elif pow(A, C) < pow(B, C):
        print("<")
    else:
        print("=")

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print("=")
    elif a >= 0 and b >= 0:
        if a > b:
            print(">")
        else:
            print("<")
    elif a >= 0 and b < 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                print(">")
            else:
                print("<")
        else:
            print(">")
    elif a < 0 and b >= 0:
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
Suggestion 8

def pow(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        return pow(a, b/2) * pow(a, b/2)
    else:
        return pow(a, b/2) * pow(a, b/2) * a

=======
Suggestion 9

def main():
    A, B, C = map(int, input().split())
    if A == B:
        print('=')
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if abs(A) < abs(B):
                print('<')
            else:
                print('>')
        else:
            if abs(A) < abs(B):
                print('>')
            else:
                print('<')
    elif A < 0 and B >= 0:
        if C % 2 == 0:
            if abs(A) < B:
                print('<')
            else:
                print('>')
        else:
            print('<')
    elif A >= 0 and B < 0:
        if C % 2 == 0:
            if A < abs(B):
                print('<')
            else:
                print('>')
        else:
            print('>')
    else:
        if A < B:
            print('<')
        else:
            print('>')

=======
Suggestion 10

def solve(a, b, c):
    if a < 0 and b < 0:
        if c % 2 == 0:
            if abs(a) > abs(b):
                return '<'
            elif abs(a) < abs(b):
                return '>'
            else:
                return '='
        else:
            if abs(a) > abs(b):
                return '>'
            elif abs(a) < abs(b):
                return '<'
            else:
                return '='
    elif a < 0 and b > 0:
        if c % 2 == 0:
            return '<'
        else:
            return '<'
    elif a > 0 and b < 0:
        if c % 2 == 0:
            return '>'
        else:
            return '<'
    elif a > 0 and b > 0:
        if a > b:
            return '>'
        elif a < b:
            return '<'
        else:
            return '='
