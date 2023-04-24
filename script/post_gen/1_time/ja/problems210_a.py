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

def main():
    n, a, x, y = map(int, input().split())
    if n < a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 3

def main():
    n, a, x, y = map(int, input().split())
    if n > a:
        print(a*x + (n-a)*y)
    else:
        print(n*x)

=======
Suggestion 4

def main():
    N, A, X, Y = map(int, input().split())
    print(min(N, A) * X + max(0, N - A) * Y)

=======
Suggestion 5

def main():
    n, a, x, y = map(int, input().split())
    sum = 0
    for i in range(1,n+1):
        if i <= a:
            sum += x
        else:
            sum += y
    print(sum)
