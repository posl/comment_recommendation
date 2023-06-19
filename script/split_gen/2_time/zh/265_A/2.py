def solve():
    X,Y,N = map(int,input().split())
    if N % 3 == 0:
        print(int(N/3)*Y)
    elif N % 3 == 1:
        print(int(N/3)*Y+X)
    else:
        print(int(N/3)*Y+2*X)
