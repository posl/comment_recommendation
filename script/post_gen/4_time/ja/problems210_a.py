Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 2

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 3

def main():
    n, a, x, y = map(int, input().split())
    ans = 0
    if n <= a:
        ans = n * x
    else:
        ans = a * x + (n - a) * y
    print(ans)

=======
Suggestion 4

def problem210_a():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 5

def main():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(0, n - a) * y)

=======
Suggestion 6

def main():
    N, A, X, Y = map(int, input().split())
    print(min(N, A) * X + max(0, N - A) * Y)

=======
Suggestion 7

def main():
    N,A,X,Y = map(int,input().split())
    if N > A:
        print(A*X + (N-A)*Y)
    else:
        print(N*X)

=======
Suggestion 8

def get_input():
    n, a, x, y = map(int, input().split())
    return n, a, x, y
