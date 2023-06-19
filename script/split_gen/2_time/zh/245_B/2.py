def find_min_positive_integer(N, A):
    result = 0
    A.sort()
    for i in range(N):
        if A[i] > result:
            return result
        elif A[i] == result:
            result += 1
    return result
