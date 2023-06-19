Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1)
    elif x > b:
        print(0)
    else:
        print(c/(b-a))

=======
Suggestion 2

def problems242_a(a,b,c,x):
    if x<=a:
        return 1
    elif a+1<=x and x<=b:
        return c/(b-a)
    else:
        return 0

=======
Suggestion 3

def calc_prob(A, B, C, X):
    prob = 0
    if X <= A:
        prob = 1
    elif X <= B:
        prob = C / (B - A)
    else:
        prob = 0
    return prob

=======
Suggestion 4

def main():
    A,B,C,X = map(int,input().split())
    if A>X:
        print(0)
    elif B>=X>=A:
        print(1)
    else:
        print(C/(B-A))

=======
Suggestion 5

def problems242_a():
    pass

=======
Suggestion 6

def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1.0)
    elif x >= b+1:
        print(0.0)
    else:
        print(c/(b-a))

=======
Suggestion 7

def problem242_a():
    pass

=======
Suggestion 8

def func(a,b,c,x):
    if x <= a:
        return 1
    elif x > b:
        return 0
    else:
        return c/(b-a)

=======
Suggestion 9

def main():
    a,b,c,x = map(int, input().split())
    if x <= a:
        print(1)
    elif a < x and x <= b:
        print(0.5)
    else:
        print(0)

=======
Suggestion 10

def getProbability(A, B, C, X):
    if X <= A:
        return 1
    elif X > B:
        return 0
    else:
        return C/(B-A)
