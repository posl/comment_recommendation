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
    if N > A:
        print(A*X + (N-A)*Y)
    else:
        print(N*X)

=======
Suggestion 3

def buy_cabbage(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y

=======
Suggestion 4

def main():
    n,a,x,y = map(int,input().split())
    total = 0
    for i in range(1,n+1):
        if i <= a:
            total += x
        else:
            total += y
    print(total)

=======
Suggestion 5

def buy_cabbage(N, A, X, Y):
    if N > A:
        return A * X + (N - A) * Y
    else:
        return N * X

=======
Suggestion 6

def cabbage():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

=======
Suggestion 7

def solve():
    N, A, X, Y = map(int, input().split())
    return min(N, A) * X + max(N - A, 0) * Y

print(solve())

=======
Suggestion 8

def solve():
    N, A, X, Y = map(int, input().split())
    print(min(N, A) * X + max(0, N - A) * Y)

=======
Suggestion 9

def main():
    #N, A, X, Y = map(int, input().split())
    #print(N, A, X, Y)
    N, A, X, Y = 5, 3, 20, 15
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)
