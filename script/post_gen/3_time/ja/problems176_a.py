Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        print(int(N / X) * T)
    else:
        print((int(N / X) + 1) * T)

=======
Suggestion 2

def main():
    N,X,T = map(int, input().split())
    if N%X == 0:
        print(N//X*T)
    else:
        print((N//X+1)*T)

=======
Suggestion 3

def main():
    # input
    N, X, T = map(int, input().split())

    # compute
    ans = (N+X-1)//X * T

    # output
    print(ans)

=======
Suggestion 4

def main():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

=======
Suggestion 5

def main():
    n,x,t = map(int,input().split())
    if n % x == 0:
        print(int((n/x)*t))
    else:
        print(int(((n//x)+1)*t))

=======
Suggestion 6

def main():
    N, X, T = map(int, input().split())
    print(((N + X - 1) // X) * T)

=======
Suggestion 7

def main():
    N,X,T = map(int,input().split())
    if N%X == 0:
        print(int(N/X)*T)
    else:
        print(int(N/X+1)*T)

=======
Suggestion 8

def main():
    N, X, T = map(int, input().split())
    print(((N-1)//X+1)*T)

=======
Suggestion 9

def main():
    n,x,t = map(int, input().split())
    print((n+x-1)//x*t)
