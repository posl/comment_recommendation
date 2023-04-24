Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A * 60 + B < C * 60 + D:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 2

def main():
    A, B, C, D = map(int, input().split())
    if A * 60 + B < C * 60 + D:
        print("Aoki")
    else:
        print("Takahashi")

=======
Suggestion 3

def main():
    A, B, C, D = map(int, input().split())
    if A < C:
        print("Takahashi")
    elif A > C:
        print("Aoki")
    else:
        if B < D:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        print("Takahashi")
    elif a == c:
        if b < d:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Aoki")

main()

=======
Suggestion 5

def main():
    A, B, C, D = map(int, input().split())

    if A < C:
        print("Takahashi")
    elif A == C:
        if B < D:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Aoki")

=======
Suggestion 6

def main():
    A, B, C, D = map(int, input().split())
    if A == C:
        if B < D:
            print("Takahashi")
        else:
            print("Aoki")
    elif A < C:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 7

def main():
    a,b,c,d = map(int,input().split())
    if a < c:
        print("Takahashi")
    elif a > c:
        print("Aoki")
    else:
        if b < d:
            print("Takahashi")
        else:
            print("Aoki")

main()

=======
Suggestion 8

def main():
    A, B, C, D = map(int, input().split())

    if A * 60 + B < C * 60 + D:
        print('Aoki')
    else:
        print('Takahashi')

=======
Suggestion 9

def main():
    a,b,c,d = map(int,input().split())
    if a*60+b < c*60+d:
        print("Takahashi")
    else:
        print("Aoki")
