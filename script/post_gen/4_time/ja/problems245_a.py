Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A > C:
        print("Takahashi")
    elif A < C:
        print("Aoki")
    elif A == C:
        if B > D:
            print("Takahashi")
        elif B < D:
            print("Aoki")
        elif B == D:
            print("same")

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())

    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    else:
        if b > d:
            print("Takahashi")
        elif b < d:
            print("Aoki")
        else:
            print("Same")

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if a < c:
        print("Takahashi")
    elif a > c:
        print("Aoki")
    else:
        if b < d:
            print("Takahashi")
        elif b > d:
            print("Aoki")
        else:
            print("Same")

=======
Suggestion 4

def main():
    a,b,c,d = map(int, input().split())
    if a > c:
        print('Takahashi')
    elif a < c:
        print('Aoki')
    else:
        if b > d:
            print('Takahashi')
        elif b < d:
            print('Aoki')
        else:
            print('same')

=======
Suggestion 5

def main():
    A,B,C,D = map(int,input().split())
    if A > C:
        print('Takahashi')
    elif A < C:
        print('Aoki')
    else:
        if B > D:
            print('Takahashi')
        elif B < D:
            print('Aoki')
        else:
            print('Same')

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    elif b > d:
        print("Takahashi")
    elif b < d:
        print("Aoki")
    else:
        print("Same")

=======
Suggestion 7

def problem245_a():
    a, b, c, d = map(int, input().split())
    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    else:
        if b > d:
            print("Takahashi")
        elif b < d:
            print("Aoki")
        else:
            print("Same")

=======
Suggestion 8

def main():
    A, B, C, D = map(int, input().split())

    if A == C:
        if B == D:
            print("Takahashi")
        elif B > D:
            print("Takahashi")
        else:
            print("Aoki")
    elif A > C:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 9

def main():
    a,b,c,d = map(int,input().split())
    if a*60+b<c*60+d:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 10

def main():
    a,b,c,d = map(int,input().split())
    if (c*60+d)-(a*60+b) > 0:
        print("Takahashi")
    else:
        print("Aoki")
