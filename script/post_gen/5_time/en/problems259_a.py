Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(1, X):
        T += D
    for i in range(X, N):
        T += D
    print(T)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        print(T + (M - 1) * D)
    else:
        print(T + (X - 1) * D + (N - X) * D)

=======
Suggestion 3

def birthday(N, M, X, T, D):
    height = T
    for i in range(1, X):
        height += D
    for i in range(X, N):
        height += D
    return height

=======
Suggestion 4

def main():
    n, m, x, t, d = map(int, input().split())
    height = t
    for i in range(x, n):
        height += d
    for i in range(1, x):
        height += d
    print(height)

=======
Suggestion 5

def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(1, X):
        height += D
    if M < X:
        for i in range(X, N):
            height += D
    print(height)

=======
Suggestion 6

def solve(n,m,x,t,d):
    height = t
    for i in range(1,x):
        height += d
    for i in range(x,n):
        height += d
    return height

=======
Suggestion 7

def get_height(n, m, x, t, d):
    height = t
    for i in range(x, n):
        height += d
    for i in range(m, x):
        height += d
    return height

=======
Suggestion 8

def find_height(n,m,x,t,d):
    height = t
    for i in range(1,x):
        height += d
    for i in range(x,n):
        height += d
    return height

=======
Suggestion 9

def main():
    n,m,x,t,d = map(int, input().split())
    h = x * d + t
    for i in range(x+1, n):
        h += d
    for i in range(x-1, m):
        h -= d
    print(h)

=======
Suggestion 10

def problem():
    N,M,X,T,D = map(int,input().split())
    height = T
    for i in range(1,M):
        height += D
    for i in range(M,X):
        height += D
    for i in range(X,N):
        height += 0
    return height

print(problem())
