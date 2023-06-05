def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    C=list(map(int,input().split()))
    B=[0]*(M+1)
    for i in range(N+M,0,-1):
        B[M]=int((C[i]-sum([A[j]*B[j] for j in range(M)]))/A[N])
        for j in range(M):
            B[j]=B[j]+A[j]*B[M]
    print(' '.join(map(str,B)))

if __name__ == '__main__':
    main()