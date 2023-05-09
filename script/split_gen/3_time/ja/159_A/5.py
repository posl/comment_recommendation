def main():
    N,M = map(int,input().split())
    if N > M:
        N,M = M,N
    #print(N,M)
    if N == 0:
        print(M)
        return
    ans = N*(M-N) + N*(N-1)//2
    print(ans)
