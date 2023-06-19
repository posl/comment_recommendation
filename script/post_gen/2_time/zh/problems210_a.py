Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,a,x,y = map(int,input().split())
    if n<=a:
        print(n*x)
    else:
        print(a*x+(n-a)*y)

=======
Suggestion 2

def main():
    n, a, x, y = map(int, input().split())
    if n > a:
        print(a * x + (n - a) * y)
    else:
        print(n * x)

=======
Suggestion 3

def problem210_a(n, a, x, y):
    if n <= a:
        return n*x
    else:
        return a*x + (n-a)*y

=======
Suggestion 4

def solve():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y

print(solve())

=======
Suggestion 5

def main():
    N,A,X,Y = map(int,input().split())
    if N <= A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)

=======
Suggestion 6

def buy_cabbage(n, a, x, y):
    cost = 0
    if n <= a:
        cost = n * x
    else:
        cost = a * x + (n - a) * y
    return cost
