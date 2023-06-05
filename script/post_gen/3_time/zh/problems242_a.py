Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,c,x = map(int, raw_input().split())
    if x <= a:
        print 1
    elif x >= b:
        print 0
    else:
        print float(c)/(b-a)

=======
Suggestion 2

def getProbability(A, B, C, X):
    if X <= A:
        return 1
    elif X > B:
        return 0
    else:
        return C/(B-A)

=======
Suggestion 3

def main():
    A, B, C, X = map(int, input().split())
    print(C / (B-A+1) if A <= X <= B else 0)

=======
Suggestion 4

def main():
    A,B,C,X = map(int,input().split())
    if A >= X:
        print(1)
    elif A < X and X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 5

def solve(a,b,c,x):
    if x <= a:
        return 1
    elif x >= b+1:
        return 0
    else:
        return c/(b-a)

a,b,c,x = map(int, input().split())
print(solve(a,b,c,x))

=======
Suggestion 6

def main():
    A,B,C,X = map(int,input().split())
    if A >= X:
        print(1)
    elif A < X and B >= X:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 7

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif X > B:
        print(0)
    else:
        print(C / (B - A))

=======
Suggestion 8

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif x <= b:
        print(c / (b - a))
    else:
        print(0)

=======
Suggestion 9

def main():
    a,b,c,x = map(int, input().split())
    if x <= a:
        print(1)
    elif x > b:
        print(0)
    else:
        print(c/(b-a))

=======
Suggestion 10

def main():
    A,B,C,X = map(int, input().split())
    if A >= X:
        print(1.0)
    elif A < X <= B:
        print(1/C)
    else:
        print(0.0)
