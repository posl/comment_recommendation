Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)

=======
Suggestion 2

def main():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

=======
Suggestion 3

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print((n//x)*t)
    else:
        print((n//x+1)*t)

=======
Suggestion 4

def main():
    n, x, t = map(int, input().split())
    print((n + x - 1) // x * t)
main()

=======
Suggestion 5

def main():
    n, x, t = map(int, input().split(" "))
    print((n + x - 1) // x * t)

=======
Suggestion 6

def takoyaki(N,X,T):
    count = 0
    while N > 0:
        N -= X
        count += T
    return count

N,X,T = list(map(int,input().split()))
print(takoyaki(N,X,T))

=======
Suggestion 7

def takoyaki():
    n, x, t = map(int, input().split())
    print((n+x-1)//x*t)
