def get_max_stone(N, K, A):
    max_stone = 0
    for i in range(K):
        if i == 0:
            max_stone = A[i]
        elif i == K-1:
            if max_stone < N-A[K-1]:
                max_stone = N-A[K-1]
        else:
            if max_stone < A[i]-A[i-1]:
                max_stone = A[i]-A[i-1]
    return max_stone
