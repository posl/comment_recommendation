Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print("高桥")
    elif a == c:
        if b > d:
            print("高桥")
        else:
            print("青木")
    else:
        print("青木")

=======
Suggestion 2

def main():
    a, b, c, d = map(int, input().split())
    if (a * 60 + b) < (c * 60 + d):
        print("High")
    else:
        print("Low")

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if (a*60+b) < (c*60+d):
        print("高桥")
    else:
        print("青木")

=======
Suggestion 4

def get_time():
    A, B, C, D = map(int, input().split())
    return A, B, C, D

=======
Suggestion 5

def main():
    A, B, C, D = map(int, input().split())
    if (A*60+B) < (C*60+D):
        print('高桥')
    else:
        print('青木')

=======
Suggestion 6

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print('高桥')
    elif a < c:
        print('青木')
    elif b > d:
        print('高桥')
    elif b < d:
        print('青木')
    else:
        print('同時')

=======
Suggestion 7

def main():
    A,B,C,D = map(int,input().split())
    if A*60+B < C*60+D:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 8

def main():
    A,B,C,D = map(int, input().split())
    if (A > C) or (A == C and B > D):
        print("高桥")
    else:
        print("青木")

=======
Suggestion 9

def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        print("高桥")
    elif a > c:
        print("青木")
    else:
        if b < d:
            print("高桥")
        else:
            print("青木")
