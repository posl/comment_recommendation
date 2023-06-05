def main():
    N,K = map(int,input().split())
    if K == 1:
        print(N+1)
    else:
        print((N+1)*(N+2)//2)
