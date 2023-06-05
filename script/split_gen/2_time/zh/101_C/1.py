def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if K == 1:
        print(N-1)
        return
    print((N-2)//(K-1)+1)
