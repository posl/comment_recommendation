def check_same_shape(N, M, A, B, C, D):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i, j) in zip(A, B) and (i, j) not in zip(C, D):
                return False
            if (i, j) not in zip(A, B) and (i, j) in zip(C, D):
                return False
    return True
