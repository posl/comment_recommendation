Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A > C or (A == C and B > D):
        print("高桥")
    else:
        print("青木")

=======
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print("高桥")
    elif a < c:
        print("青木")
    else:
        if b > d:
            print("高桥")
        elif b < d:
            print("青木")
        else:
            print("高桥")

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if a < c or (a == c and b < d):
        print("高桥")
    else:
        print("青木")

=======
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    if (a * 60 + b) < (c * 60 + d):
        print("青木")
    else:
        print("高桥")

=======
Suggestion 5

def main():
    a, b, c, d = map(int, input().split())
    if a < c:
        print('高桥')
    elif a == c:
        if b < d:
            print('高桥')
        elif b == d:
            print('同时')
        else:
            print('青木')
    else:
        print('青木')
main()

=======
Suggestion 6

def main():
    a, b, c, d = map(int, input().split())
    if (a > c) or ((a == c) and (b > d)):
        print("高桥")
    else:
        print("青木")

=======
Suggestion 7

def problem245_a():
    a, b, c, d = map(int, input().split())
    if a < c:
        print("高桥")
    elif a > c:
        print("青木")
    elif a == c:
        if b < d:
            print("高桥")
        elif b > d:
            print("青木")
        elif b == d:
            print("高桥")

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())

    a = a*60 + b
    c = c*60 + d
    if a < c:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 9

def main():
    A, B, C, D = map(int, input().split())
    if A > C:
        print('高桥')
    elif A < C:
        print('青木')
    elif B > D:
        print('高桥')
    elif B < D:
        print('青木')
    else:
        print('同時')

=======
Suggestion 10

def main():
    A,B,C,D = map(int,input().split())
    if A < C:
        print('高桥')
    elif A > C:
        print('青木')
    elif B < D:
        print('高桥')
    elif B > D:
        print('青木')
    else:
        print('高桥')
