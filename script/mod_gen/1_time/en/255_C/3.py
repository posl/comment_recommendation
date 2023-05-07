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

if __name__ == '__main__':
    main()