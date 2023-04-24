Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1.0)
    elif a < x <= b:
        print(c/(b-a))
    else:
        print(0.0)

=======
Suggestion 3

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif A < X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 4

def main():
    A,B,C,X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X and X <= B:
        print(C/(B-A))
    else:
        print(0.0)

=======
Suggestion 5

def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1)
    elif x <= b:
        print(c/(b-a))
    else:
        print(0)

=======
Suggestion 6

def main():
    a,b,c,x = map(int, input().split())
    if a <= x and x <= b:
        print(c/b)
    else:
        print(0)

=======
Suggestion 7

def calc_prob(a,b,c,x):
    if x <= a:
        return 1
    elif a < x <= b:
        return c/(b-a)
    else:
        return 0

a,b,c,x = map(int,input().split())
print(calc_prob(a,b,c,x))
