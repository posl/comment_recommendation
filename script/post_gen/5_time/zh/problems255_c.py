Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print("inf")
        return
    if D < 0:
        D = -D
        A = -A
        X = -X
    if N == 1:
        if X == A:
            print(0)
        else:
            print("inf")
        return
    if N == 2:
        if X == A or X == A+D:
            print(0)
        else:
            print("inf")
        return
    if X < A:
        print("inf")
        return
    if X == A:
        print(1)
        return
    if (X - A) % D == 0:
        print((X - A) // D)
    else:
        print("inf")

=======
Suggestion 2

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a)%d == 0:
            if (x-a)/d >= 0 and (x-a)/d < n:
                print(0)
            else:
                print(1)
        else:
            if (x-a)/d >= 0 and (x-a)/d < n:
                print(1)
            else:
                print(2)

=======
Suggestion 3

def solve(x,a,d,n):
    if d==0:
        if x==a:
            return 0
        else:
            return 1
    if n==1:
        if x==a:
            return 0
        else:
            return 1
    if n==2:
        if x==a:
            return 0
        else:
            return 2
    if d>0:
        if x<a:
            return 1
        else:
            if (x-a)%d==0:
                return (x-a)//d
            else:
                return (x-a)//d+1
    if d<0:
        if x>a:
            return 1
        else:
            if (a-x)%d==0:
                return (a-x)//d
            else:
                return (a-x)//d+1

=======
Suggestion 4

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if (X - A) % D == 0:
            print((X - A) // D)
        else:
            print("invalid")

=======
Suggestion 5

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(0)
        return
    if D > 0:
        if X < A:
            print(A-X)
            return
        else:
            if (X-A)%D == 0:
                print((X-A)//D)
                return
            else:
                print(-1)
                return
    if D < 0:
        if X > A:
            print(X-A)
            return
        else:
            if (A-X)%(-D) == 0:
                print((A-X)//(-D))
                return
            else:
                print(-1)
                return

=======
Suggestion 6

def main():
    x,a,d,n=map(int,input().split())
    if d==0:
        if x==a:
            print(0)
        else:
            print(1)
    else:
        if (x-a)%d==0 and (x-a)//d>=0:
            print((x-a)//d)
        else:
            print(1+(x-a)//d)

=======
Suggestion 7

def solve(x,a,d,n):
    if x < a:
        return a-x
    elif x == a:
        return 0
    else:
        if d == 0:
            return 0
        else:
            if x < a:
                return a-x
            else:
                if (x-a)%d == 0:
                    return (x-a)//d
                else:
                    return (x-a)//d + 1

=======
Suggestion 8

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if n == 1:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if n == 2:
        if x == a or x == a+d:
            print(0)
        else:
            print(1)
        return
    if (x-a)%d == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 9

def solve(X,A,D,N):
    if D == 0:
        if X == A:
            return 0
        else:
            return -1
    if N == 1:
        if X == A:
            return 0
        else:
            return -1
    if N == 2:
        if X == A:
            return 0
        elif X == A+D:
            return 1
        else:
            return -1
    if N >= 3:
        if X == A:
            return 0
        elif (X-A)%D == 0:
            return int((X-A)/D)
        elif (X-A-D)%D == 0:
            return int((X-A-D)/D)+1
        else:
            return -1
