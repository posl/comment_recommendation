def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
    else:
        if (X-A)%D == 0 and (X-A)//D >= 0:
            if N > (X-A)//D:
                print(N-(X-A)//D)
            else:
                print(0)
        else:
            print(-1)
