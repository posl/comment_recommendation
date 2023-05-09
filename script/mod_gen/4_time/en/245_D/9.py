def main():
    #N,M=map(int,input().split())
    #A=list(map(int,input().split()))
    #C=list(map(int,input().split()))
    N,M=1,2
    A=[2,1]
    C=[12,14,8,2]
    B=[0]*M
    for i in range(N+M):
        for j in range(M+1):
            if i-j<N+1 and i-j>=0:
                B[j-1]+=A[i-j]*C[i]
    print(*B)

if __name__ == '__main__':
    main()