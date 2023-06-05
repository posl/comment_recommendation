Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        print(1/C)
    else:
        print(0.0)

=======
Suggestion 2

def main():
    a,b,c,x = map(int, input().split())
    if x <= a:
        print(1)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0)

=======
Suggestion 3

def solve():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif A < X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 4

def problem242_a():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1.0)
    elif a+1 <= x <= b:
        print(c/(b-a))
    else:
        print(0.0)

=======
Suggestion 5

def problems242_a():
    a,b,c,x=map(int,input().split())
    if x<=a:
        print(1.0)
    elif a<x<=b:
        print(c/(b-a))
    else:
        print(0.0)

=======
Suggestion 6

def problems242_a():
    A,B,C,X=map(int,input().split())
    if X<A:
        print(0)
    elif X>=A and X<=B:
        print(1)
    else:
        print(C/(B-A))

=======
Suggestion 7

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif A+1 <= X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 8

def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1.0)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0.0)

=======
Suggestion 9

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif X > B:
        print(0)
    else:
        print(C/(B-A))

=======
Suggestion 10

def main():
    A,B,C,X = map(int, input().split())
    if A >= X:
        print(1.0)
        return
    if X > B:
        print(0.0)
        return
    if C == 0:
        print(0.0)
        return
    if A+1 == B:
        if X == A+1:
            print(1.0)
        else:
            print(0.0)
        return
    if X == A+1:
        print(1.0)
        return
    if X == B:
        print(1.0)
        return
    if X < A+C+1:
        print(1.0)
        return
    print(C/(B-A-1))
    return
