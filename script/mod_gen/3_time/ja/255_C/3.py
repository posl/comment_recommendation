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

if __name__ == '__main__':
    main()