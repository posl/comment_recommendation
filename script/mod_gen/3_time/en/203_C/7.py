def main():
    N,K=map(int,input().split())
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=map(int,input().split())
    A.append(1000000000000000000)

if __name__ == '__main__':
    main()