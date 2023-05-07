def solve(N,M,A,C):
    B = [0]*(M+1)
    B[M] = C[N+M]//A[N]
    for i in range(M):
        B[M-1-i] = (C[N+M-1-i]-sum(B[M-i:])*A[N-1-i])//A[N]
    return B

if __name__ == '__main__':
    solve()