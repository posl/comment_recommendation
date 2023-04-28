Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 2

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    if S == U:
        A -= 1
    else:
        B -= 1

    print(A, B)

=======
Suggestion 3

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        print(a-1, b)
    elif u == t:
        print(a, b-1)
    else:
        print(a, b)

=======
Suggestion 4

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    elif u == t:
        b -= 1
    print(a,b)

=======
Suggestion 5

def main():
    S,T = map(str,input().split())
    A,B = map(int,input().split())
    U = str(input())
    if U == S:
        A -= 1
    else:
        B -= 1
    print(A,B)

=======
Suggestion 6

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    if u == s:
        print(a-1,b)
    else:
        print(a,b-1)

=======
Suggestion 7

def main():
    S,T = map(str,input().split())
    A,B = map(int,input().split())
    U = str(input())
    if U == S:
        A -= 1
    elif U == T:
        B -= 1
    print(A,B)

=======
Suggestion 8

def main():
    s,t = map(str,input().split())
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a,b)

=======
Suggestion 9

def main():
    S,T = map(str,input().split())
    A,B = map(int,input().split())
    U = str(input())

    if S == U:
        A = A - 1
    else:
        B = B - 1

    print(A,B)

=======
Suggestion 10

def main():
    #input
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()

    #compute
    if u == s:
        a -= 1
    elif u == t:
        b -= 1

    #output
    print(a,b)
