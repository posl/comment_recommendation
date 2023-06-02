Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B,C,D = map(int, input().split())
    if A > C:
        print("高桥")
    elif A == C and B > D:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 2

def main():
    a,b,c,d = map(int, input().split())
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
            print("青木")

=======
Suggestion 3

def main():
    a, b, c, d = map(int, input().split())
    time_a = a*60 + b
    time_b = c*60 + d
    if time_a < time_b:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 4

def main():
    A,B,C,D = map(int,input().split())
    if A > C:
        print("高桥")
    elif A < C:
        print("青木")
    elif A == C:
        if B > D:
            print("高桥")
        elif B < D:
            print("青木")
        elif B == D:
            print("高桥")

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    if a < c:
        print("高桥")
    elif a > c:
        print("青木")
    else:
        if b < d:
            print("高桥")
        elif b > d:
            print("青木")
        else:
            print("高桥")

=======
Suggestion 6

def main():
    a,b,c,d = map(int, input().split())
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
Suggestion 7

def main():
    a,b,c,d = map(int,input().split())
    if a>c:
        print("高桥")
    elif a<c:
        print("青木")
    elif a==c:
        if b>d:
            print("高桥")
        elif b<d:
            print("青木")
        elif b==d:
            print("高桥")

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())
    if a > c or (a == c and b > d):
        print("高桥")
    else:
        print("青木")

=======
Suggestion 9

def get_up_early(a,b,c,d):
    if a<c:
        print("高桥")
    elif a==c:
        if b<d:
            print("高桥")
        elif b==d:
            print("同一时间")
        else:
            print("青木")
    else:
        print("青木")
    return

=======
Suggestion 10

def getup_time():
    A,B,C,D = map(int,input().split())
    if A > C:
        print("高桥")
    elif A < C:
        print("青木")
    elif A == C:
        if B > D:
            print("高桥")
        elif B < D:
            print("青木")
        elif B == D:
            print("高桥")

getup_time()
