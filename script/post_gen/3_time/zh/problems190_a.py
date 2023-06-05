Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem190_a(a, b, c):
    if c == 0:
        if a > b:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if b > a:
            return 'Aoki'
        else:
            return 'Takahashi'

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if B > A:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 3

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
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if b > a:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
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
Suggestion 6

def getWinner():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if A >= B:
            print('Takahashi')
        else:
            print('Aoki')

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
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

=======
Suggestion 8

def solve(A,B,C):
    if C==0:
        if A>B:
            print("Takahashi")
        else:
            print("Aoki")
    if C==1:
        if A>=B:
            print("Takahashi")
        else:
            print("Aoki")
