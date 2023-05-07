def main():
    N,X,Y = map(int,input().split())
    for k in range(1,N):
        if k == 1:
            print(N-1)
        else:
            print((N-k)*(N-k-1)//2 - (N-Y-k+1)*(N-X-k+1) + (X-1)*(Y-k))
