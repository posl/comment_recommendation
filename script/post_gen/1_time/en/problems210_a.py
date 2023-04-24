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
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N*X)
    else:
        print(A*X + (N-A)*Y)

main()

=======
Suggestion 3

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(X * A + Y * (N - A))

=======
Suggestion 4

def main():
    n, a, x, y = map(int, input().split())
    print(x * min(n, a) + y * max(0, n - a))

=======
Suggestion 5

def main():
    n,a,x,y = map(int,input().split())
    if n < a:
        print(n*x)
    else:
        print((n-a)*y+a*x)

=======
Suggestion 6

def main():
    # read input
    n,a,x,y = map(int, input().split())
    # calculate
    if n <= a:
        result = n*x
    else:
        result = a*x + (n-a)*y
    # output
    print(result)
