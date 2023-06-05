def buyGoods(N, M, A):
    #print(N, M, A)
    A.sort()
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    if M >= sum:
        return 0
    else:
        for i in range(M):
            A[N-1-i] = A[N-1-i]//2
        return buyGoods(N, M, A)

if __name__ == '__main__':
    buyGoods()