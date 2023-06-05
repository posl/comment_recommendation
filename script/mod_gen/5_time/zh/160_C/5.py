def solve(K,N,A):
    #print(K,N,A)
    #print(A[0],K-A[N-1])
    #print(max(A[0],K-A[N-1]))
    #print((K-A[N-1])+(A[N-1]-A[0]))
    return min(max(A[0],K-A[N-1]),(K-A[N-1])+(A[N-1]-A[0]))

if __name__ == '__main__':
    solve()