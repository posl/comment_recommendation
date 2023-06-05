def main():
    D,N = map(int,input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(100*101)
        else:
            print(100*N)
    else:
        if N == 100:
            print(100*100*101)
        else:
            print(100*100*N)
