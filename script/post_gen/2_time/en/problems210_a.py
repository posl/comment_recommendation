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
        print(X*A + Y*(N-A))
    else:
        print(X*N)

=======
Suggestion 3

def main():
    n,a,x,y = map(int,input().split())
    if n <= a:
        print(n*x)
    else:
        print(a*x+(n-a)*y)

=======
Suggestion 4

def main():
    n,a,x,y = map(int,input().split())
    if n > a:
        print(a*x+(n-a)*y)
    else:
        print(n*x)

=======
Suggestion 5

def main():
    n,a,x,y = map(int,input().split())
    print(x*min(n,a) + y*max(0,n-a))

main()

=======
Suggestion 6

def main():
    #get input
    N,A,X,Y = map(int,input().split())
    #calculate cost
    if N <= A:
        cost = N*X
    else:
        cost = A*X + (N-A)*Y
    #print cost
    print(cost)
