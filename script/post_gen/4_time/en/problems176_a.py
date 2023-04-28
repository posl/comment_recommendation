Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        print(N // X * T)
    else:
        print((N // X + 1) * T)

=======
Suggestion 2

def main():
    N, X, T = map(int, input().split())
    print((N + X - 1) // X * T)

=======
Suggestion 3

def takoyaki(n,x,t):
    if(n%x==0):
        return (n//x)*t
    else:
        return (n//x+1)*t

n,x,t = map(int,input().split())
print(takoyaki(n,x,t))

=======
Suggestion 4

def takoyaki(N,X,T):
    if N%X==0:
        return (N/X)*T
    else:
        return ((N//X)+1)*T

=======
Suggestion 5

def main():
    n,x,t = [int(i) for i in input().split()]
    print((n+x-1)//x*t)

=======
Suggestion 6

def takoyaki():
    # read in input
    n, x, t = map(int, input().split())
    # print(n, x, t)
    # find number of times x fits into n
    # print(n // x)
    # find remainder
    # print(n % x)
    # if remainder is 0, then we are done
    # if remainder is not 0, then we need to add 1 to n // x
    # return n // x * t
    return ((n // x) + (1 if n % x else 0)) * t

print(takoyaki())
