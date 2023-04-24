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
    else:
        if D > 0:
            if X > A:
                if X - A < D * (N - 1):
                    print(min(abs(X - A), abs(X - (A + D * (N - 1)))))
                else:
                    print(abs(X - (A + D * (N - 1))))
            else:
                if A - X < D * (N - 1):
                    print(min(abs(X - A), abs(X - (A - D * (N - 1)))))
                else:
                    print(abs(X - (A - D * (N - 1))))
        else:
            if X < A:
                if A - X < abs(D) * (N - 1):
                    print(min(abs(X - A), abs(X - (A + D * (N - 1)))))
                else:
                    print(abs(X - (A + D * (N - 1))))
            else:
                if X - A < abs(D) * (N - 1):
                    print(min(abs(X - A), abs(X - (A - D * (N - 1)))))
                else:
                    print(abs(X - (A - D * (N - 1))))

=======
Suggestion 2

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X - A))
    else:
        if D > 0:
            if X < A:
                print(abs(X - A))
            elif X > A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(0)
        else:
            if X > A:
                print(abs(X - A))
            elif X < A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
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
        if D > 0:
            if X < A:
                print(abs(X-A))
            elif X > A+(N-1)*D:
                print(abs(X-(A+(N-1)*D)))
            else:
                print(0)
        else:
            if X > A:
                print(abs(X-A))
            elif X < A+(N-1)*D:
                print(abs(X-(A+(N-1)*D)))
            else:
                print(0)

=======
Suggestion 4

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
    else:
        if D > 0:
            if X >= A:
                if (X-A) % D == 0:
                    print(0)
                else:
                    print(min(abs((X-A) % D),abs(D - (X-A) % D)))
            else:
                if (A-X) % D == 0:
                    print(A-X)
                else:
                    print(min(abs((A-X) % D),abs(D - (A-X) % D)))
        else:
            if X <= A:
                if (A-X) % abs(D) == 0:
                    print(0)
                else:
                    print(min(abs((A-X) % abs(D)),abs(abs(D) - (A-X) % abs(D))))
            else:
                if (X-A) % abs(D) == 0:
                    print(X-A)
                else:
                    print(min(abs((X-A) % abs(D)),abs(abs(D) - (X-A) % abs(D))))

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        print(abs(x - a))
        return
    if a <= x <= a + (n - 1) * d:
        print(0)
        return
    if x < a:
        print(min(abs(x - a), abs(x - a - n * d)))
        return
    if x > a + (n - 1) * d:
        print(min(abs(x - a - (n - 1) * d), abs(x - a - n * d)))
        return

=======
Suggestion 7

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X - A))
        return
    if D > 0:
        if X <= A:
            print(A - X)
            return
        elif X >= A + (N - 1) * D:
            print(X - A - (N - 1) * D)
            return
        else:
            print(min(X - A, A + (N - 1) * D - X))
            return
    else:
        if X >= A:
            print(X - A)
            return
        elif X <= A + (N - 1) * D:
            print(A + (N - 1) * D - X)
            return
        else:
            print(min(A - X, X - A - (N - 1) * D))
            return

main()

=======
Suggestion 8

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        print(abs(x-a))
    elif d > 0:
        if x < a:
            print(a-x)
        elif x > a+d*(n-1):
            print(x-a-d*(n-1))
        else:
            print(min(x-a,x-a-d*(n-1))%d)
    else:
        if x < a+d*(n-1):
            print(a+d*(n-1)-x)
        elif x > a:
            print(x-a)
        else:
            print(min(a-x,a+d*(n-1)-x)%abs(d))

=======
Suggestion 9

def main():
    x,a,d,n=map(int,input().split())
    if d==0:
        print(abs(x-a))
        return
    if n==1:
        print(abs(x-a))
        return
    if d>0:
        if x<a:
            print(min(abs(a-x),abs(a+d*(n-1)-x)))
            return
        if x>a+d*(n-1):
            print(abs(a+d*(n-1)-x))
            return
        print(min(abs(a-x)+d*(n-1),abs(a+d*(n-1)-x)))
        return
    if d<0:
        if x>a:
            print(min(abs(a-x),abs(a+d*(n-1)-x)))
            return
        if x<a+d*(n-1):
            print(abs(a+d*(n-1)-x))
            return
        print(min(abs(a-x)+d*(n-1),abs(a+d*(n-1)-x)))
        return

=======
Suggestion 10

def get_input():
    return list(map(int,input().split()))
