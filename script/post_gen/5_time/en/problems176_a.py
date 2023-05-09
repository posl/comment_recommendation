Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        print(int(N/X) * T)
    else:
        print((int(N/X) + 1) * T)

=======
Suggestion 2

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        print(int(N / X * T))
    else:
        print(int((N // X + 1) * T))

=======
Suggestion 3

def takoyaki():
    N, X, T = map(int, input().split())
    if (N % X) == 0:
        return int(N / X) * T
    else:
        return (int(N / X) + 1) * T

print(takoyaki())

=======
Suggestion 4

def takoyaki():
    N,X,T = map(int, input().split())
    if N % X == 0:
        return (N//X)*T
    else:
        return (N//X + 1)*T

print(takoyaki())

=======
Suggestion 5

def main():
    n, x, t = map(int, input().split())
    print((n+x-1)//x * t)

=======
Suggestion 6

def main():
    n,x,t = map(int, input().split())
    print(((n-1)//x+1)*t)

=======
Suggestion 7

def main():
    N,X,T = map(int, input().split())
    print(int((N+X-1)/X)*T)

=======
Suggestion 8

def solve():
    N,X,T = map(int, input().split())
    print((N//X + (N%X!=0))*T)

=======
Suggestion 9

def main():
    n,x,t = map(int,input().split())
    print((n//x + 1) * t)

=======
Suggestion 10

def takoyaki(N,X,T):
    return (N//X + 1) * T
