def main():
    N,P,Q,R=map(int,input().split())
    A=list(map(int,input().split()))
    ans=0
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    ans=max(ans,A[i]*P+A[j]*Q+A[k]*R+A[l])
    print(ans)

if __name__ == '__main__':
    main()