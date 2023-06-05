def dot_product(A, B):
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result

if __name__ == '__main__':
    dot_product()