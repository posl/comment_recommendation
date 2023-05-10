Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, x = map(int, input().split())
    if a <= x <= b:
        print(c/b)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1.0)
    elif a < x <= b:
        print(c / (b - a))
    else:
        print(0.0)

=======
Suggestion 3

def main():
    a,b,c,x = map(int, input().split())
    if a <= x <= b:
        print(c/b)
    else:
        print(0)

main()

=======
Suggestion 4

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1.0)
    elif x > b:
        print(0.0)
    else:
        print(c / (b - a))

=======
Suggestion 5

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif X >= B:
        print(0.0)
    else:
        print((B - X) / (B - A))

=======
Suggestion 6

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif x <= b:
        print((b-x)/(b-a))
    else:
        print(0)

=======
Suggestion 7

def solve():
    A, B, C, X = map(int, input().split())
    if X<=A:
        print(1.0)
        return
    if X>B:
        print(0.0)
        return
    if A==B:
        print(0.0)
        return
    if C==0:
        print(0.0)
        return
    if C==1:
        print(1.0/(B-A))
        return
    if C==B-A:
        print(1.0)
        return
    if C==2:
        print(1.0/(B-A)*(1.0/(B-A-1)))
        return
    if C==3:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2)))
        return
    if C==4:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3)))
        return
    if C==5:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4)))
        return
    if C==6:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4))*(1.0/(B-A-5)))
        return
    if C==7:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4))*(1.0/(B-A-5))*(1.0/(B-A-6)))
        return
    if C==8:
        print(1.0/(B-A)*(1.0/(B-A-1))*(1.0/(B-A-2))*(1.0/(B-A-3))*(1.0/(B-A-4))*(1.0/(B-A-5))*(1.0/(B-A-6))*(1.0/(B-A-7)))

=======
Suggestion 8

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1.0)
    elif x <= b:
        print(c / (b - a))
    else:
        print(0.0)

=======
Suggestion 9

def solve():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        p = (B-X)/(B-A)
        print(p)
    else:
        print(0.0)

=======
Suggestion 10

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X and X <= B:
        print(C/(B-A))
    else:
        print(0.0)
