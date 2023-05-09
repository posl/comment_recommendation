def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    B = [0]*N
    for i in range(N):
        B[i] = A[i]
        if i == 0:
            B[i] = A[i] - A[N-1]
        else:
            B[i] = A[i] - A[i-1]
    #print(B)
    C = [0]*N
    for i in range(N):
        C[i] = B[i]*2
    #print(C)
    D = [0]*N
    for i in range(N):
        D[i] = C[i] + C[i-1]
    #print(D)
    E = [0]*N
    for i in range(N):
        E[i] = int(D[i]/2)
    print(*E)

if __name__ == '__main__':
    main()