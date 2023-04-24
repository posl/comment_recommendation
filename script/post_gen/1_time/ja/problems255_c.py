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

    if X == A:
        print(0)
        return

    if X < A:
        if D < 0:
            if X < A + D * (N - 1):
                print(abs(X - A))
            else:
                print(abs(X - (A + D * (N - 1))))
        else:
            print(abs(X - A))
    else:
        if D > 0:
            if X > A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(abs(X - A))
        else:
            print(abs(X - A))

=======
Suggestion 2

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
        return
    elif D > 0:
        if X < A:
            print(A-X)
            return
        elif X >= A+(N-1)*D:
            print(X-A-(N-1)*D)
            return
        else:
            if (X-A) % D == 0:
                print(0)
                return
            else:
                print(min(X-A-(X-A)//D*D, A+(X-A)//D*D+D-X))
                return
    else:
        if X > A:
            print(X-A)
            return
        elif X <= A-(N-1)*D:
            print(A-X-(N-1)*D)
            return
        else:
            if (X-A) % D == 0:
                print(0)
                return
            else:
                print(min(X-A-(X-A)//D*D, A+(X-A)//D*D+D-X))
                return

=======
Suggestion 3

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(abs(x-a))
    elif d > 0:
        if x < a:
            print(a-x)
        elif x > a+d*(n-1):
            print(x-(a+d*(n-1)))
        else:
            print(min(x-a,a+d*(n-1)-x))
    else:
        if x > a:
            print(x-a)
        elif x < a+d*(n-1):
            print(a+d*(n-1)-x)
        else:
            print(min(a-x,x-(a+d*(n-1))))

=======
Suggestion 4

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(abs(x-a))
    else:
        if x == a:
            print(0)
        elif x < a:
            if d > 0:
                print(abs(a-x))
            else:
                if (a-x)%d == 0:
                    print(0)
                else:
                    print((a-x)%d)
        else:
            if d < 0:
                print(abs(a-x))
            else:
                if (x-a)%d == 0:
                    print(0)
                else:
                    print(d-(x-a)%d)

=======
Suggestion 5

def main():
    X,A,D,N = map(int,input().split())

    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
        return

    if D > 0:
        if X < A:
            print(abs(X-A))
            return
        if X > A + D*(N-1):
            print(abs(X-A-D*(N-1)))
            return

        if (X-A)%D == 0:
            print(0)
        else:
            if (X-A)//D < N-1:
                print(min(abs(X-A-D*((X-A)//D+1)),abs(X-A-D*((X-A)//D))))
            else:
                print(abs(X-A-D*((X-A)//D)))

    if D < 0:
        if X > A:
            print(abs(X-A))
            return
        if X < A + D*(N-1):
            print(abs(X-A-D*(N-1)))
            return

        if (X-A)%D == 0:
            print(0)
        else:
            if (X-A)//D < N-1:
                print(min(abs(X-A-D*((X-A)//D+1)),abs(X-A-D*((X-A)//D))))
            else:
                print(abs(X-A-D*((X-A)//D)))

=======
Suggestion 6

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        print(abs(x-a))
    elif d > 0:
        if x < a:
            print(a-x)
        elif x > a + d*(n-1):
            print(x-(a+d*(n-1)))
        else:
            print(min(x-a,a+d*(n-1)-x))
    else:
        if x > a:
            print(x-a)
        elif x < a + d*(n-1):
            print(a+d*(n-1)-x)
        else:
            print(min(a-x,x-(a+d*(n-1))))

=======
Suggestion 7

def main():
    X,A,D,N=map(int,input().split())
    if D==0:
        print(abs(X-A))
    elif D>0:
        if X<A:
            print(A-X)
        elif X>A+D*(N-1):
            print(X-(A+D*(N-1)))
        else:
            print(min(X-A,A+D*(N-1)-X))
    else:
        if X>A:
            print(X-A)
        elif X<A+D*(N-1):
            print(A+D*(N-1)-X)
        else:
            print(min(X-A,A+D*(N-1)-X))

=======
Suggestion 8

def main():
    x,a,d,n = map(int,input().split())
    ans = 0
    if d == 0:
        ans = abs(x-a)
    else:
        if x == a:
            ans = 0
        else:
            if d > 0:
                if x < a:
                    ans = abs(x-a)
                else:
                    if (x-a)%d == 0:
                        ans = 0
                    else:
                        ans = min(abs(x-a)%d,abs(x-a)%d-d)
            else:
                if x > a:
                    ans = abs(x-a)
                else:
                    if (x-a)%d == 0:
                        ans = 0
                    else:
                        ans = min(abs(x-a)%d,abs(x-a)%d-d)
    print(ans)

=======
Suggestion 9

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X-A))
        return
    elif D > 0:
        # 0回以上の操作でXを良い数にする時、必要な操作の最小回数
        # 0回の操作でXを良い数にする場合
        # 1回以上の操作でXを良い数にする場合
        # 0回の操作でXを良い数にできる場合は、X-Aが最小の場合
        # 1回以上の操作でXを良い数にする場合は、X-AがDで割り切れる場合
        if (X-A) % D == 0:
            print(0)
            return
        else:
            print(min(abs((X-A) % D), abs(D-(X-A) % D)))
            return
    else:
        # D < 0の場合
        # 0回以上の操作でXを良い数にする時、必要な操作の最小回数
        # 0回の操作でXを良い数にする場合
        # 1回以上の操作でXを良い数にする場合
        # 0回の操作でXを良い数にできる場合は、X-Aが最小の場合
        # 1回以上の操作でXを良い数にする場合は、X-AがDで割り切れる場合
        if (X-A) % D == 0:
            print(0)
            return
        else:
            print(min(abs((X-A) % D), abs(D-(X-A) % D)))
            return

=======
Suggestion 10

def main():
    X, A, D, N = map(int, input().split())

    # 1. Dが0の場合
    if D == 0:
        # 1.1. AとXが等しい場合
        if A == X:
            print(0)
        # 1.2. AとXが等しくない場合
        else:
            print(abs(X - A))

    # 2. Dが0でない場合
    else:
        # 2.1. AとXが等しい場合
        if A == X:
            print(0)
        # 2.2. AとXが等しくない場合
        else:
            # 2.2.1. XがAより小さい場合
            if X < A:
                #
