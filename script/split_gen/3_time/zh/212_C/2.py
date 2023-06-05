def min_diff(A,B):
    A.sort()
    B.sort()
    i = 0
    j = 0
    min_diff = 999999999
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            return 0
        elif A[i] > B[j]:
            min_diff = min(min_diff,A[i]-B[j])
            j += 1
        else:
            min_diff = min(min_diff,B[j]-A[i])
            i += 1
    return min_diff
