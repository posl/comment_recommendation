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
        if A < B:
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
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
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
Suggestion 4

def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A < B:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 5

def main():
    # input
    A, B, C = map(int, input().split())

    # compute

    # output
    if C == 0:
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
Suggestion 6

def main():
    a,b,c = map(int, input().split())
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
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if c == 0:
        if a - b >= 1:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if b - a >= 1:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if c==0:
        if a>b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a>=b:
            print('Takahashi')
        else:
            print('Aoki')

=======
Suggestion 9

def main():
    a,b,c = map(int, input().split())
    if a > b:
        print("Takahashi")
    elif a < b:
        print("Aoki")
    elif c == 0:
        print("Aoki")
    elif c == 1:
        print("Takahashi")
