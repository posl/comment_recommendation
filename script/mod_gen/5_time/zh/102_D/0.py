def main():
    N=int(input())
    A=list(map(int,input().split()))
    S=sum(A)
    ans=float('inf')
    s=0
    for i in range(N-1):
        s+=A[i]
        ans=min(ans,abs(S-2*s))
    print(ans)

if __name__ == '__main__':
    main()