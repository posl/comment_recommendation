def main():
    N = int(input())
    A = list(map(int,input().split()))
    Asum = [0]*(N+1)
    for i in range(N):
        Asum[i+1] = Asum[i] + A[i]
    #print(Asum)
    ans = 10**9
    for i in range(1,N-1):
        for j in range(i+1,N):
            #print(i,j)
            P = Asum[i]
            Q = Asum[j] - Asum[i]
            R = Asum[N] - Asum[j]
            S = Asum[N] - Asum[i]
            #print(P,Q,R,S)
            ans = min(ans,max(P,Q,R,S)-min(P,Q,R,S))
    print(ans)

if __name__ == '__main__':
    main()