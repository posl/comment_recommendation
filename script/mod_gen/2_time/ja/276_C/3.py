def next_permutation(A):
    N = len(A)
    i = N - 1
    while i > 0 and A[i - 1] >= A[i]:
        i -= 1
    if i == 0:
        return False
    j = N - 1
    while A[j] <= A[i - 1]:
        j -= 1
    A[i - 1], A[j] = A[j], A[i - 1]
    j = N - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    next_permutation()