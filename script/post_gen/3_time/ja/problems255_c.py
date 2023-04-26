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
            if X < A:
                print(abs(X - A))
            elif X > A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(min(abs(X - A), abs(X - (A + D * (N - 1)))))
        else:
            if X > A:
                print(abs(X - A))
            elif X < A + D * (N - 1):
                print(abs(X - (A + D * (N - 1))))
            else:
                print(min(abs(X - A), abs(X - (A + D * (N - 1)))))

=======
Suggestion 2

def main():
    X,A,D,N=map(int,input().split())
    if D==0:
        if X==A:
            print(0)
        else:
            print(abs(X-A))
    else:
        if X>=A:
            if D>0:
                if (X-A)%D==0:
                    print(0)
                else:
                    print(min((X-A)%D,D-(X-A)%D))
            else:
                print(abs(X-A))
        else:
            if D<0:
                if (A-X)%abs(D)==0:
                    print(0)
                else:
                    print(min((A-X)%abs(D),abs(D)-(A-X)%abs(D)))
            else:
                print(abs(X-A))

=======
Suggestion 3

def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X-A))
    elif D < 0:
        D = -D
        A = -A
        X = -X
        print(min(abs(X-A), abs(X-A-D*(N-1))))
    else:
        print(min(abs(X-A), abs(X-A-D*(N-1))))

=======
Suggestion 4

def main():
    #入力
    X,A,D,N = map(int,input().split())

    #処理
    if D == 0:
        if X == A:
            print(0)
        else:
            print(abs(X-A))
    else:
        if D > 0:
            if X < A:
                print(abs(X-A))
            else:
                if (X-A) % D == 0:
                    print(0)
                else:
                    print(min(abs(X-(A+D*((X-A)//D))),abs(X-(A+D*((X-A)//D+1)))))
        else:
            if X > A:
                print(abs(X-A))
            else:
                if (X-A) % D == 0:
                    print(0)
                else:
                    print(min(abs(X-(A+D*((X-A)//D))),abs(X-(A+D*((X-A)//D-1)))))

=======
Suggestion 5

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(abs(X-A))
        return
    elif D > 0:
        if X < A:
            print(A-X)
        elif X > A+(N-1)*D:
            print(X-(A+(N-1)*D))
        else:
            print(min(X-A,(A+(N-1)*D)-X))
    else:
        if X > A:
            print(X-A)
        elif X < A+(N-1)*D:
            print((A+(N-1)*D)-X)
        else:
            print(min(A-X,X-(A+(N-1)*D)))

=======
Suggestion 6

def main():
    x,a,d,n = map(int,input().split())
    if d==0:
        print(abs(x-a))
        return
    if d>0:
        if x<=a:
            print(a-x)
            return
        if x>=a+d*(n-1):
            print(x-a-d*(n-1))
            return
        print(min(abs(x-a-d*(n-1)),abs(x-a)))
        return
    if d<0:
        if x>=a:
            print(x-a)
            return
        if x<=a+d*(n-1):
            print(a-x-d*(n-1))
            return
        print(min(abs(x-a-d*(n-1)),abs(x-a)))
        return

=======
Suggestion 7

def main():
    x,a,d,n=map(int,input().split())
    if d>0:
        if x<=a:
            print(abs(x-a))
        elif x>=a+d*(n-1):
            print(abs(x-a-d*(n-1)))
        else:
            print(min(abs(x-a),abs(x-a-d*(n-1))))
    elif d==0:
        if x==a:
            print(0)
        else:
            print(abs(x-a))
    else:
        if x>=a:
            print(abs(x-a))
        elif x<=a+d*(n-1):
            print(abs(x-a-d*(n-1)))
        else:
            print(min(abs(x-a),abs(x-a-d*(n-1))))

=======
Suggestion 8

def main():
    X, A, D, N = map(int, input().split())
    # X, A, D, N = map(int, input().split())
    # print(X, A, D, N)

    # X, A, D, N = 6, 2, 3, 3
    # X, A, D, N = 0, 0, 0, 1
    # X, A, D, N = 998244353, -10, -20, 30
    # X, A, D, N = -555555555555555555, -1000000000000000000, 1000000, 1000000000000

    # 1. AからXまでの差分を求める
    diff = X - A
    # print(diff)

    # 2. AからXまでの差分をDで割った商と余りを求める
    # 商をq、余りをrとする
    q, r = diff // D, diff % D
    # print(q, r)

    # 3. 余りが0の場合、qがN以下の場合はqを出力する
    if r == 0 and q <= N:
        print(q)
        return

    # 4. 余りが0でない場合、q+1がN以下の場合はq+1を出力する
    if r != 0 and q + 1 <= N:
        print(q + 1)
        return

    # 5. それ以外の場合は-1を出力する
    print(-1)

=======
Suggestion 9

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        print(abs(x-a))
    else:
        if x < a:
            if d < 0:
                print(abs(x-a)+abs(a+(n-1)*d))
            else:
                print(abs(x-a))
        elif x > a:
            if d > 0:
                print(abs(x-a)+abs(a+(n-1)*d))
            else:
                print(abs(x-a))
        else:
            print(abs(a+(n-1)*d))

=======
Suggestion 10

def main():
    X, A, D, N = map(int, input().split())
    # X が A + (N - 1) * D 以上の場合
    if X >= A + (N - 1) * D:
        print(X - (A + (N - 1) * D))
    # X が A + (N - 1) * D 以下の場合
    else:
        # X が A + (N - 2) * D 以上の場合
        if X >= A + (N - 2) * D:
            print(0)
        # X が A + (N - 2) * D 以下の場合
        else:
            print(min(abs(X - (A + (N - 2) * D)), abs(X - (A + (N - 1) * D))))
