Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 2

def buy_cabbage(N, A, X, Y):
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y

=======
Suggestion 3

def main():
    n,a,x,y = map(int, input().split())
    if n > a:
        print(a*x + (n-a)*y)
    else:
        print(n*x)

=======
Suggestion 4

def buy_cabbage(N, A, X, Y):
    if N <= A:
        return X * N
    else:
        return A * X + (N - A) * Y

=======
Suggestion 5

def problem():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(0, n - a) * y)

=======
Suggestion 6

def cabbage():
    n, a, x, y = input().split()
    n = int(n)
    a = int(a)
    x = int(x)
    y = int(y)

    if n > a:
        print(a*x + (n-a)*y)
    else:
        print(n*x)

=======
Suggestion 7

def main():
    #n, a, x, y = map(int, input().split())
    n, a, x, y = 5, 3, 20, 15
    if n > a:
        print(a * x + (n - a) * y)
    else:
        print(n * x)
