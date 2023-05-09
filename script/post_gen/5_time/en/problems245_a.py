Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A > C:
        print("Takahashi")
    elif A < C:
        print("Aoki")
    else:
        if B > D:
            print("Takahashi")
        elif B < D:
            print("Aoki")
        else:
            print("Draw")

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        print("Aoki")
    elif a > c:
        print("Takahashi")
    else:
        if b < d:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 3

def main():
    A, B, C, D = map(int, input().split())
    if A > C:
        print("Takahashi")
    elif A < C:
        print("Aoki")
    elif B > D:
        print("Takahashi")
    elif B < D:
        print("Aoki")
    else:
        print("Same")

=======
Suggestion 4

def main():
    a,b,c,d = map(int, input().split())
    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    else:
        if b > d:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 5

def main():
    a, b, c, d = map(int, input().split())
    if a == c:
        if b <= d:
            print("Takahashi")
        else:
            print("Aoki")
    elif a < c:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
    if a == c:
        if b < d:
            print("Takahashi")
        else:
            print("Aoki")
    elif a < c:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 7

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print("Takahashi")
    elif a == c:
        if b > d:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Aoki")

=======
Suggestion 8

def main():
    A,B,C,D = map(int, input().split())
    if (A*60 + B) < (C*60 + D):
        print('Takahashi')
    elif (A*60 + B) > (C*60 + D):
        print('Aoki')
    else:
        print('Same time')
