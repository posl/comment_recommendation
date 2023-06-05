def missing_number(A):
    A.sort()
    for i in range(len(A)):
        if A[i] != i:
            return i
    return len(A)
