Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a < b:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 2

def main():
    A,B,C = map(int,input().split())
    if C == 1:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 3

def solve():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if B > A:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 4

def Takahashi_or_Aoki(A,B,C):
    if C == 0:
        if A > B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if A > B:
            return 'Aoki'
        else:
            return 'Takahashi'

=======
Suggestion 5

def main():
    A,B,C = input().split()
    if int(C) == 0:
        if int(A) > int(B):
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if int(B) > int(A):
            print("Aoki")
        el

=======
Suggestion 6

def solve():
    A,B,C = map(int,input().split())
    if (C == 0):
        if (A > B):
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if (B > A):
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    elif C == 1:
        if B > A:
            print("Aoki")
        else:

=======
Suggestion 8

def solve():
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if b > a:
            print('Aoki')
        else:
            print('Takahashi')
