def myfun(A, x, k):
    for i in range(0, len(A)):
        if A[i] == x:
            k -= 1
            if k == 0:
                return i + 1
    return -1
