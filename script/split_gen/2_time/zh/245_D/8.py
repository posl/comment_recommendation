def get_max_diff(A, B):
    max_diff = 0
    for i in range(len(A)):
        diff = abs(A[i] - B[i])
        if diff > max_diff:
            max_diff = diff
    return max_diff
