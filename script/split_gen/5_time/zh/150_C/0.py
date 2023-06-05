def getPermutationCount(n):
    if n == 1:
        return 1
    else:
        return n*getPermutationCount(n-1)
