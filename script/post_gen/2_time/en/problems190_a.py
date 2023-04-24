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
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
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

main()

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
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
    a, b, c = map(int, input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a >= b:
            print('Takahashi')
        else:
            print('Aoki')

=======
Suggestion 5

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
Suggestion 6

def main():
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

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a == b:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")
    elif a > b:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print("Aoki" if c else "Takahashi")
    else:
        print("Takahashi" if a > b else "Aoki")

=======
Suggestion 9

def main():
    A, B, C = map(int, input().split())
    if A > B:
        print("Takahashi")
    elif A < B:
        print("Aoki")
    elif A == B:
        if C == 0:
            print("Aoki")
        elif C == 1:
            print("Takahashi")
