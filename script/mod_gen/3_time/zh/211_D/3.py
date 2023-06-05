def main():
    N,M=map(int,input().split())
    A=[0]*M
    B=[0]*M
    for i in range(M):
        A[i],B[i]=map(int,input().split())
    print(N,M,A,B)
    return 0

if __name__ == '__main__':
    main()