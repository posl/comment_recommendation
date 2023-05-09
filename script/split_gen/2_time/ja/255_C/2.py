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
