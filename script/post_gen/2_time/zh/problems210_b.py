Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def buy_cabbage(n,a,x,y):
    if n<=a:
        return n*x
    else:
        return a*x+(n-a)*y

=======
Suggestion 2

def problems210_a():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 3

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 4

def main():
    n, a, x, y = map(int, input().split())
    if n > a:
        print(a*x+(n-a)*y)
    else:
        print(n*x)

=======
Suggestion 5

def main():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n*x)
    else:
        print(a*x + (n-a)*y)

=======
Suggestion 6

def main():
    n, a, x, y = map(int, input().split())
    ans = 0
    if n > a:
        ans = a * x + (n - a) * y
    else:
        ans = n * x
    print(ans)
