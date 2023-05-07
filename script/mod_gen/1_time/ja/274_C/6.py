def main():
    N=int(input())
    A=list(map(int,input().split()))
    B = [0] * (2*N+1)
    for i in range(N):
        B[2*i+1] = A[i]
        B[2*i+2] = A[i]
    for i in range(2*N,0,-1):
        if i%2==1:
            B[i//2] = B[i]
    for i in range(2*N+1):
        print(B[i])

if __name__ == '__main__':
    main()