def min_diff(A, B):
    A.sort()
    B.sort()
    i, j = 0, 0
    min_diff = abs(A[0] - B[0])
    while i < len(A) and j < len(B):
        min_diff = min(min_diff, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return min_diff

if __name__ == '__main__':
    min_diff()