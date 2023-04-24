Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A * 60 + B < C * 60 + D:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    if a * 60 + b < c * 60 + d:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 3

def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        print("Takahashi")
    elif a > c:
        print("Aoki")
    else:
        if b < d:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 4

def main():
    A, B, C, D = map(int, input().split())
    if A*60+B < C*60+D:
        print("Aoki")
    else:
        print("Takahashi")

=======
Suggestion 5

def main():
    A, B, C, D = map(int, input().split())

    if A < C:
        print("Takahashi")
    elif A > C:
        print("Aoki")
    else:
        if B < D:
            print("Takahashi")
        elif B > D:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
    if a*60+b < c*60+d:
        print('Aoki')
    else:
        print('Takahashi')

=======
Suggestion 7

def main():
    a, b, c, d = map(int, input().split())
    if a == c and b == d:
        print("Takahashi")
    elif a == c and b > d:
        print("Takahashi")
    elif a == c and b < d:
        print("Aoki")
    elif a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")

=======
Suggestion 8

def main():
    a, b, c, d = map(int, input().split())
    if a > c:
        print("Aoki")
    elif a == c:
        if b >= d:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Takahashi")

=======
Suggestion 9

def main():
    #入力
    A,B,C,D = map(int, input().split())
    #処理
    if A < C:
        print("Takahashi")
    elif A == C:
        if B < D:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Aoki")
