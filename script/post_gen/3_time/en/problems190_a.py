Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if B >= A:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 2

def main():
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
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if A == B:
        if C == 0:
            print("Aoki")
        else:
            print("Takahashi")
    elif A > B:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if (a > b and c == 0) or (a < b and c == 1):
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a > b:
        print("Takahashi")
    elif a == b:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a > b:
        print('Takahashi')
    elif a < b:
        print('Aoki')
    else:
        if c == 0:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 7

def main():
    A,B,C = map(int,input().split())
    if C == 0 and A > B:
        print("Takahashi")
    elif C == 1 and A >= B:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    if c == 1:
        if a == b:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        if a == b:
            print("Takahashi")
        else:
            print("Aoki")
