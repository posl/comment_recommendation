def solve():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    #print(N,K,P)
    for i in range(K-1,N):
        print(sorted(P[:i+1])[-K])
