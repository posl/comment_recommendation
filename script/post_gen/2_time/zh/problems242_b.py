Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif A+1 <= X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 2

def main():
    a,b,c,x = map(int,input().split())
    if a > x:
        print(0.0)
    elif a <= x <= b:
        print(1/c)
    else:
        print(0.0)

=======
Suggestion 3

def main():
    a,b,c,x = map(int,input().split())
    if x <= a:
        print(1)
    elif x <= b:
        print(c/(b-a))
    else:
        print(0)

=======
Suggestion 4

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X >= B:
        print(0)
    else:
        print(C/(B-A))

=======
Suggestion 5

def main():
    A,B,C,X = [int(x) for x in input().split()]
    if X <= A:
        print(1)
    elif X > B:
        print(0)
    else:
        print(C/(B-A))

=======
Suggestion 6

def main():
    a, b, c, x = map(int, input().split())
    print(c / (b - a + 1) if a <= x <= b else 0)

=======
Suggestion 7

def main():
    A,B,C,X = map(int,input().split())
    count=0
    if A<=X:
        count+=1
    if A+1<=X and X<=B:
        count+=C
    print(count/(B-A))

=======
Suggestion 8

def problems242_a():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X > B:
        print(0)
    else:
        print(C/(B-A))

=======
Suggestion 9

def get_probability(A, B, C, X):
    if X <= A:
        return 1
    elif X <= B:
        return C / (B - A)
    else:
        return 0
