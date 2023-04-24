Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(M, N):
        if i < X:
            T += D
        else:
            break
    print(T)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(X, N):
        height += D
    for i in range(0, X):
        height += D
    print(height)

=======
Suggestion 3

def takahashi_height(N, M, X, T, D):
    height = T
    for i in range(1, X):
        height += D
    for i in range(X, N):
        height += D
    return height

=======
Suggestion 4

def main():
    N,M,X,T,D = map(int, input().split())
    if M < X:
        print(T+(M-1)*D)
    else:
        print(T+(X-1)*D+(N-X)*D)

=======
Suggestion 5

def solve():
    N,M,X,T,D = [int(x) for x in input().split()]
    height = T
    for i in range(1,X):
        height += D
    for i in range(X,N):
        height += D
    print(height)

=======
Suggestion 6

def main():
    n,m,x,t,d = map(int, input().split())
    for i in range(m):
        if i < x:
            t += d
        else:
            break
    print(t)

=======
Suggestion 7

def solve(n, m, x, t, d):
    for i in range(x, n):
        t = t + d
    for i in range(0, m):
        t = t - d
    return t

n, m, x, t, d = map(int, input().split())

print(solve(n, m, x, t, d))

=======
Suggestion 8

def problem():
    n,m,x,t,d = map(int, input().split())
    for i in range(m):
        if i < x:
            t += d
    print(t)

=======
Suggestion 9

def main():
    N,M,X,T,D = map(int, input().split())
    for i in range(M,N):
        if i == X:
            X += D
        T += X
    print(T)

=======
Suggestion 10

def main():
    n,m,x,t,d = map(int, input().split())
    print(t + (n-x)*d if m > x else t + (m-1)*d)
