def get_min_xor(A,N):
    min_xor = 2**30
    for i in range(N-1):
        xor = A[i] ^ A[i+1]
        if xor < min_xor:
            min_xor = xor
    return min_xor
N = int(input())
A = list(map(int, input().split()))
print(get_min_xor(A,N))
