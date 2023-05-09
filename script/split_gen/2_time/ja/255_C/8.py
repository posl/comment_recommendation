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
