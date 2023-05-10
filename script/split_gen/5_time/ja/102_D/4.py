def main():
    N=int(input())
    A=list(map(int,input().split()))
    for i in range(1,N):
        A[i]+=A[i-1]
    ans=10**9
    for i in range(N-3):
        ans=min(ans,abs(A[i]-2*A[i+1]+A[-1]))
    print(ans)
main()
