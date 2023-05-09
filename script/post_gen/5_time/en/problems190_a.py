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
        if a > b:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 2

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
Suggestion 3

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
Suggestion 4

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
Suggestion 5

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
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    if c == 0:
        if a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a < b:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 7

def problem190_a():
    # Get input
    A, B, C = map(int, input().split())

    # Solve
    if C == 0:
        A -= 1
        if A >= B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        B -= 1
        if B >= A:
            print('Aoki')
        else:
            print('Takahashi')
