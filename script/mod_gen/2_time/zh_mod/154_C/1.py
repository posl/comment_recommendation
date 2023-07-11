def is_pairwise_different(A):
    A.sort()
    for i in range(1, len(A)):
        if A[i-1] == A[i]:
            return False
    return True

if __name__ == '__main__':
    is_pairwise_different()