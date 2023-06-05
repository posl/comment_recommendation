def minDiff(A, B):
    A.sort()
    B.sort()
    a, b = 0, 0
    min_diff = abs(A[0] - B[0])
    while a < len(A) and b < len(B):
        min_diff = min(min_diff, abs(A[a] - B[b]))
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
    return min_diff
