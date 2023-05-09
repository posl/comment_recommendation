def find_greatest_multiple(N,K,D,A):
    #print('N=',N)
    #print('K=',K)
    #print('D=',D)
    #print('A=',A)
    #print('N-K+1=',N-K+1)
    #print('A[N-K+1:]=',A[N-K+1:])
    #print('max(A[N-K+1:])=',max(A[N-K+1:]))
    if max(A[N-K+1:])%D == 0:
        return max(A[N-K+1:])
    else:
        return -1

if __name__ == '__main__':
    find_greatest_multiple()