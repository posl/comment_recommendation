def find_max(A):
    max = A[0]
    for i in range(1,len(A)):
        if A[i] > max:
            max = A[i]
    return max
