Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X - A))
        return
    elif D > 0:
        if X < A:
            print(A - X)
            return
        elif X >= A + D * (N - 1):
            print(X - (A + D * (N - 1)))
            return
        else:
            i = (X - A) // D
            if (X - A) % D == 0:
                print(0)
                return
            else:
                print(min(abs(X - (A + D * i)), abs(X - (A + D * (i + 1)))))
                return
    elif D < 0:
        if X > A:
            print(X - A)
            return
        elif X <= A + D * (N - 1):
            print(abs(X - (A + D * (N - 1))))
            return
        else:
            i = (X - A) // D
            if (X - A) % D == 0:
                print(0)
                return
            else:
                print(min(abs(X - (A + D * i)), abs(X - (A + D * (i - 1)))))
                return

=======
Suggestion 2

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
    else:
        if X < A:
            print(abs(X-A))
        elif X > A+(N-1)*D:
            print(abs(X-A-(N-1)*D))
        else:
            print(0)

=======
Suggestion 3

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
    else:
        if X < A:
            if D < 0:
                print((A-X)//D)
            else:
                print((A-X)//D+1)
        elif X > A+(N-1)*D:
            if D < 0:
                print((X-A-(N-1)*D)//(-D)+1)
            else:
                print((X-A-(N-1)*D)//D)
        else:
            print(0)

=======
Suggestion 4

def main():
    X, A, D, N = map(int, input().split())

    if D == 0:
        print(abs(X - A))
        return

    if D > 0:
        if X < A:
            print(A - X)
            return

        if X > A + (N - 1) * D:
            print(X - (A + (N - 1) * D))
            return

        print(0)
        return

    if X > A:
        print(X - A)
        return

    if X < A + (N - 1) * D:
        print(abs(X - (A + (N - 1) * D)))
        return

    print(0)

=======
Suggestion 5

def main():
    X, A, D, N = map(int, input().split())

    if D == 0:
        print(abs(X - A))
        return

    if D > 0:
        if X < A:
            print(A - X)
            return
        elif X > A + (N - 1) * D:
            print(X - A - (N - 1) * D)
            return
        else:
            print(min(X - A, A + (N - 1) * D - X))
            return
    else:
        if X > A:
            print(X - A)
            return
        elif X < A + (N - 1) * D:
            print(A + (N - 1) * D - X)
            return
        else:
            print(min(A - X, X - A - (N - 1) * D))
            return

=======
Suggestion 6

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X - A))
        return
    if D > 0:
        if X <= A:
            print(A - X)
            return
        if X < A + D * (N - 1):
            print(0)
            return
        print(X - A - D * (N - 1))
        return
    if D < 0:
        if X >= A:
            print(X - A)
            return
        if X > A + D * (N - 1):
            print(0)
            return
        print(A + D * (N - 1) - X)
        return

=======
Suggestion 7

def main():
    X, A, D, N = map(int, input().split())
    S = [A + D * i for i in range(N)]
    if X in S:
        print(0)
    else:
        if X < min(S):
            print(min(S) - X)
        elif X > max(S):
            print(X - max(S))
        else:
            print(min(X - min(S), max(S) - X))

=======
Suggestion 8

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(abs(X-A))
    elif D > 0:
        print(min(abs(X-A),abs(X-(A+D*(N-1)))))
    else:
        print(min(abs(X-A),abs(X-(A+D*(N-1)))))

=======
Suggestion 9

def main():
    X,A,D,N = map(int,input().split())
    if N==0:
        print(0)
        return
    if D==0:
        if X==A:
            print(0)
            return
        else:
            print(abs(X-A))
            return
    if D>0:
        if X<A:
            print(A-X)
            return
        if X>A+(N-1)*D:
            print(X-(A+(N-1)*D))
            return
        else:
            print(min(abs(X-A),abs(X-(A+(N-1)*D))))
            return
    if D<0:
        if X>A:
            print(X-A)
            return
        if X<A+(N-1)*D:
            print(abs(X-(A+(N-1)*D)))
            return
        else:
            print(min(abs(X-A),abs(X-(A+(N-1)*D))))
            return

=======
Suggestion 10

def calc_good_num(a,d,n):
    return a+(n-1)*d
