def main():
    #input
    N, Q = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))
        L[i] = A[i][0]
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    
    #solve
    Ls = [0] * (N + 1)
    for i in range(N):
        Ls[i + 1] = Ls[i] + L[i]
    
    #output
    for i in range(Q):
        print(A[S[i] - 1][T[i] - Ls[S[i] - 1] + Ls[S[i] - 1 - 1] + 1])

if __name__ == '__main__':
    main()