Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,a,x,y = map(int,input().split())
    if n <= a:
        print(n*x)
    else:
        print(a*x+(n-a)*y)

=======
Suggestion 2

def main():
    N, A, X, Y = map(int, input().split())
    if N > A:
        print(A * X + (N - A) * Y)
    else:
        print(N * X)

=======
Suggestion 3

def cabbage(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y

=======
Suggestion 4

def calc_cost(n, a, x, y):
    cost = 0
    if n <= a:
        cost = n * x
    else:
        cost = a * x + (n - a) * y
    return cost

=======
Suggestion 5

def solution():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 6

def calc_price(head, a, x, y):
    if head <= a:
        return head * x
    else:
        return a * x + (head - a) * y

=======
Suggestion 7

def main():
    N,A,X,Y = map(int,input().split())
    if N<=A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)

=======
Suggestion 8

def calc_cost(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y

=======
Suggestion 9

def solve():
    N,A,X,Y=map(int,input().split())
    if N<=A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)
