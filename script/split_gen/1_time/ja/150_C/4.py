def getPermutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in getPermutation(n-1)] + [p + [n] for p in getPermutation(n-1)]
