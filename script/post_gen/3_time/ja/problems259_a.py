Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(X, M):
        T += D
    print(T)

=======
Suggestion 2

def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(x, m):
        t += d
    print(t)

=======
Suggestion 3

def main():
    n, m, x, t, d = map(int, input().split())
    h = t
    for i in range(x, n):
        h += d
    for i in range(x, m):
        h -= d
    print(h)

=======
Suggestion 4

def main():
    N, M, X, T, D = map(int, input().split())
    height = T
    for i in range(X, N):
        height += D
    print(height)

=======
Suggestion 5

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        for i in range(M, X):
            T += D
    else:
        for i in range(X, M):
            T -= D
    print(T)

=======
Suggestion 6

def main():
    n,m,x,t,d = map(int,input().split())
    for i in range(x):
        t += d
    for i in range(x,n):
        t += d
    print(t)

=======
Suggestion 7

def solve(n, m, x, t, d):
    for i in range(x):
        t -= d
    for i in range(x, m):
        t += d
    return t

n, m, x, t, d = map(int, input().split())
print(solve(n, m, x, t, d))

=======
Suggestion 8

def main():
    n,m,x,t,d = map(int,input().split())
    a = t
    for i in range(m,x):
        a += d
    for i in range(x,n):
        a += d
    print(a)
main()

=======
Suggestion 9

def get_input_data():
    n,m,x,t,d = map(int, input().split())
    return n,m,x,t,d
