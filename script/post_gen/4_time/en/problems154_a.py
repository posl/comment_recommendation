Synthesizing 10/10 solutions (Duplicates hidden)

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
    if U == S:
        A -= 1
    else:
        B -= 1
    print(A, B)

=======
Suggestion 3

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        A -= 1
    else:
        B -= 1
    print(A,B)

=======
Suggestion 4

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        A -= 1
    elif T == U:
        B -= 1
    print(A, B)

=======
Suggestion 5

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A = A - 1
    else:
        B = B - 1
    print(A, B)

=======
Suggestion 6

def main():
    S, T = map(str, input().split())
    A, B = map(int, input().split())
    U = str(input())
    if S == U:
        A -= 1
    elif T == U:
        B -= 1
    print(A, B)

=======
Suggestion 7

def main():
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()

    if S == U:
        A = A - 1
    elif T == U:
        B = B - 1

    print(A, B)

=======
Suggestion 8

def main():
    #S, T, A, B, U = input().split()
    #A = int(A)
    #B = int(B)
    #print(A-1, B)
    
    S, T = input().split()
    A, B = input().split()
    U = input()
    if U == S:
        print(int(A)-1, B)
    else:
        print(A, int(B)-1)
