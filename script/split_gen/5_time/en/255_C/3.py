def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if D > 0:
            if X < A:
                print(1)
            elif X == A:
                print(0)
            else:
                if (X-A)%D == 0:
                    print((X-A)//D)
                else:
                    print((X-A)//D+1)
        else:
            if X > A:
                print(1)
            elif X == A:
                print(0)
            else:
                if (X-A)%D == 0:
                    print((X-A)//D)
                else:
                    print((X-A)//D+1)
