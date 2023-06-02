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

def main():
    a,b,c,x = map(int,input().split())
    if x<=a:
        print(1)
    elif x>=b:
        print(0)
    else:
        print(c/(b-a))
main()

=======
Suggestion 3

def getTshirt():
    A,B,C,X = map(int,input().split())
    if X <= A:
        return 1.0
    elif X <= B:
        return C/(B-A)
    else:
        return 0.0

print(getTshirt())

=======
Suggestion 4

def main():
    A, B, C, X = map(int, input().split())
    print(C/(B-A) if A <= X <= B else 0)

=======
Suggestion 5

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X >= A+1 and X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 6

def solve():
    a,b,c,x=map(int,input().split())
    if x<=a:
        print(1)
    elif a+1<=x<=b:
        print(c/(b-a))
    else:
        print(0)

=======
Suggestion 7

def problems242_a():
    A,B,C,X = map(int,input().split())
    if X<=A:
        print(1.0)
    elif X>A and X<B:
        print(C/(B-A))
    else:
        print(0.0)

=======
Suggestion 8

def main():
    A,B,C,X = map(int,input().split())
    if X <= A:
        print(1)
    elif X > B:
        print(0)
    else:
        print(C/(B-A))

=======
Suggestion 9

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif X <= B:
        print(C/(B-A))
    else:
        print(0)

=======
Suggestion 10

def get_tshirt_probability(A, B, C, X):
    if X <= A:
        return 1
    elif X <= B:
        return C / (B - A)
    else:
        return 0
