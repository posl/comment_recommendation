Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    if a<c:
        print("Takahashi")
    elif a>c:
        print("Aoki")
    else:
        if b<d:

=======
Suggestion 2

def main():
    A, B, C, D = map(int, input().split())
    if A < C:
        print('Takahashi')
    elif A > C:
        print('Aoki')
    else:

=======
Suggestion 3

def main():
    a,b,c,d = map(int, input().split())
    if a>b:
        print("Takahashi")
    elif a<b:
        print("Aoki")
    else:
        if c>d:

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    if a < c:
        print("Takahashi")
    elif a > c:
        print("Aoki")
    else:

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print("Takahashi")
    elif a < c:
        print("Aoki")
    else:

=======
Suggestion 6

def main():
    # 读取输入
    A, B, C, D = map(int, input().split())
    if A > C:
        print('Takahashi')
    elif A < C:
        print('Aoki')

=======
Suggestion 7

def main():
    a,b,c,d = map(int,input().split())
    if (a > c) or (a == c and b > d):
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 8

def main():
    A,B,C,D = map(int,input().split())
    if A > C:
        print("Takahashi")
    elif A == C:
        if B > D:
            print("Takahashi")

=======
Suggestion 9

def main():
    a,b,c,d=map(int,input().split())
    if a<c or (a==c and b<=d):
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 10

def main():
    A,B,C,D = map(int,input().split())
    if A == C:
        if B > D:
            print('Takahashi')
        else:
            print('Aoki')
    elif A >
