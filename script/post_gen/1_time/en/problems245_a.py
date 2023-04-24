Synthesizing 10/10 solutions

=======
Suggestion 1

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
            print("Draw")

=======
Suggestion 2

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
            print("Same")

=======
Suggestion 3

def main():
    A, B, C, D = map(int, input().split())
    if (A * 60 + B) < (C * 60 + D):
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 4

def main():
    a,b,c,d = map(int, input().split())
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
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
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
Suggestion 6

def main():
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    d = int(inp[3])
    if a == c:
        if b < d:
            print('Takahashi')
        else:
            print('Aoki')
    elif a < c:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 7

def main():
    a,b,c,d = map(int, input().split())
    if a > c or (a == c and b > d):
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 8

def main():
    A,B,C,D = map(int,input().split())
    if A==C:
        if B<D:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A<C:
            print("Aoki")
        else:
            print("Takahashi")

=======
Suggestion 9

def main():
    A,B,C,D = map(int,input().split())
    if A*60+B < C*60+D:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 10

def main():
    A,B,C,D = map(int,input().split())
    if A>B:
        print('Takahashi')
    elif A==B:
        if C>D:
            print('Takahashi')
        elif C==D:
            print('Draw')
        else:
            print('Aoki')
    else:
        print('Aoki')
