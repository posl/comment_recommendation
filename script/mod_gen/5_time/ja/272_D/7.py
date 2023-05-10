def main():
    N,M = map(int,input().split())
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(0 if i==j==0 else -1,end=' ')
            print()
        return
    C = [0]*(N*N+1)
    for i in range(N):
        for j in range(N):
            C[(i+1)*(j+1)] = 1
    for k in range(2,N*N+1):
        if C[k] == 1:
            for l in range(2,N*N//k+1):
                C[k*l] = 0
    D = [0]*(N*N+1)
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i*i+j*j] = 1
    for k in range(2,N*N+1):
        if D[k] == 1:
            for l in range(2,N*N//k+1):
                D[k*l] = 0
    for i in range(N):
        for j in range(N):
            if C[i*N+j+1] == 1 and D[i*i+j*j] == 1:
                print(-1,end=' ')
            else:
                print(i+j,end=' ')
        print()

if __name__ == '__main__':
    main()