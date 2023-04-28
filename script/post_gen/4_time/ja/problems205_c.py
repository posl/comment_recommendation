Synthesizing 10/10 solutions

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
    if a == b:
        print("=")
    elif c % 2 == 0:
        if abs(a) == abs(b):
            print("=")
        elif abs(a) > abs(b):
            print(">")
        else:
            print("<")
    elif c % 2 == 1:
        if a > b:
            print(">")
        else:
            print("<")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if c%2 == 0:
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
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if c%2 == 0:
        if abs(a) == abs(b):
            print('=')
        elif abs(a) > abs(b):
            print('>')
        else:
            print('<')
    else:
        if a == b:
            print('=')
        elif a > b:
            print('>')
        else:
            print('<')

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
    if C%2==0:
        if abs(A)==abs(B):
            print('=')
        elif abs(A)>abs(B):
            print('>')
        else:
            print('<')
    else:
        if A==B:
            print('=')
        elif A>B:
            print('>')
        else:
            print('<')

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if c%2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print("=")
    elif a < b:
        print("<")
    else:
        print(">")

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if c%2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print("=")
    elif a > b:
        print(">")
    else:
        print("<")

=======
Suggestion 8

def main():
    A,B,C = map(int, input().split())
    if A == B:
        print("=")
    elif C%2 == 0:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
            print(">")
        else:
            print("<")
    else:
        if A > B:
            print(">")
        else:
            print("<")

=======
Suggestion 9

def main():
    a,b,c = map(int, input().split())

    if(c%2==0):
        if(abs(a)>abs(b)):
            print(">")
        elif(abs(a)<abs(b)):
            print("<")
        else:
            print("=")
    else:
        if(a>b):
            print(">")
        elif(a<b):
            print("<")
        else:
            print("=")

=======
Suggestion 10

def main():
    #n = int(input())
    #s = input()
    #n, k = map(int, input().split())
    a, b, c = map(int, input().split())
    #al = list(map(int, input().split()))
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #print(n, k)
    #print(a)
    #print(al)
    #print(a)
    #print(b)
    #print(c)
    if c % 2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print('=')
    elif a > b:
        print('>')
    else:
        print('<')
    return
