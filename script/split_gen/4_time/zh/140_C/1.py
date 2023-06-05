def maxsum(A):
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        return max(A)
    else:
        maxA = max(A)
        i = A.index(maxA)
        if i == 0:
            return maxA + maxsum(A[i+1:])
        elif i == len(A)-1:
            return maxA + maxsum(A[:i])
        else:
            return maxA + max(maxsum(A[:i]), maxsum(A[i+1:]))
