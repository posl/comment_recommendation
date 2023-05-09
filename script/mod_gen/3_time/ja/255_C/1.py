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

if __name__ == '__main__':
    main()