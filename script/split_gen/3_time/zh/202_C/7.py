def solution1(N, A, B, C):
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                count += 1
    return count
