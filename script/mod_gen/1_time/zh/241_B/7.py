def solve(N,M,A,B):
    if M>N:
        return False
    A.sort()
    B.sort()
    for i in range(M):
        if B[i]<A[N-M+i]:
            return False
    return True

if __name__ == '__main__':
    solve()