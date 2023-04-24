Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

main()

=======
Suggestion 2

def main():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 3

def main():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

=======
Suggestion 4

def main():
    N,X,T = input().split()
    N = int(N)
    X = int(X)
    T = int(T)
    if N%X == 0:
        print(int(N/X)*T)
    else:
        print(int(N/X+1)*T)

=======
Suggestion 5

def takoyaki():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

takoyaki()

=======
Suggestion 6

def takoyaki(N, X, T):
    if N <= X:
        return T
    else:
        return (N // X) * T + takoyaki(N % X, X, T)

=======
Suggestion 7

def takoyaki():
    n,x,t = map(int, input().split())
    if n%x==0:
        print(n//x*t)
    else:
        print(n//x*t+t)

=======
Suggestion 8

def takoyaki(n, x, t):
    return (n // x + 1) * t if n % x else n // x * t
