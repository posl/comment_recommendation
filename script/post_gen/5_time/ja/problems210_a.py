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
    if N > A:
        return A * X + (N - A) * Y
    else:
        return N * X

N, A, X, Y = map(int, input().split())
print(buy_cabbage(N, A, X, Y))

=======
Suggestion 3

def main():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n-a) * y)

=======
Suggestion 4

def main():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(n - a, 0) * y)

=======
Suggestion 5

def get_input():
    n, a, x, y = map(int, input().split())
    return n, a, x, y

=======
Suggestion 6

def solve():
    #n, a, x, y = map(int, input().split())
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 7

def main():
    n,a,x,y = map(int, input().split())
    if n < a:
        print(n*x)
    else:
        print(a*x+(n-a)*y)
