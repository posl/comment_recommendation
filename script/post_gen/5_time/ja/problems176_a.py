Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n/x)*t)
    else:
        print((int(n/x)+1)*t)

=======
Suggestion 2

def main():
    # input
    n, x, t = map(int, input().split())
    # compute
    time = 0
    if n % x == 0:
        time = n // x * t
    else:
        time = n // x * t + t
    # output
    print(time)

=======
Suggestion 3

def main():
    n,x,t = map(int, input().split())
    print(((n + x - 1) // x) * t)
    return

=======
Suggestion 4

def main():
    N,X,T = map(int,input().split())
    if (N % X) == 0:
        print(int(N/X)*T)
    else:
        print((int(N/X)+1)*T)

=======
Suggestion 5

def main():
    n,x,t = map(int, input().split())
    print(((n+x-1)//x)*t)

=======
Suggestion 6

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(n // x * t)
    else:
        print((n // x + 1) * t)

=======
Suggestion 7

def solve():
    n, x, t = map(int, input().split())
    if n % x == 0:
        return n // x * t
    else:
        return (n // x + 1) * t

print(solve())

=======
Suggestion 8

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        print(int(N/X) * T)
    else:
        print((int(N/X) + 1) * T)

=======
Suggestion 9

def main():
    N,X,T = map(int,input().split())
    if N % X == 0:
        print((N//X)*T)
    else:
        print(((N//X)+1)*T)
