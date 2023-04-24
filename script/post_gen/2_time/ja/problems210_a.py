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
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

=======
Suggestion 3

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(X * N)
    else:
        print(X * A + Y * (N - A))

=======
Suggestion 4

def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(X*N)
    else:
        print(A*X+(N-A)*Y)

=======
Suggestion 5

def main():
    #入力
    N,A,X,Y=map(int,input().split())
    #キャベツを買う
    if N<=A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)
