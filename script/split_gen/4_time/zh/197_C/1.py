def getMinXOR(N, A):
    # N = int(input())
    # A = [int(i) for i in input().split()]
    min_xor = 2**30
    for i in range(1,N):
        xor = 0
        for j in range(i):
            xor ^= A[j]
        for j in range(i,N):
            xor |= A[j]
        min_xor = min(min_xor, xor)
    return min_xor
