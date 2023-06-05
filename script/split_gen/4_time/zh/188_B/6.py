def dot_product(A, B):
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result
