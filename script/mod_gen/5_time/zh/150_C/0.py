def getPermutationCount(n):
    if n == 1:
        return 1
    else:
        return n*getPermutationCount(n-1)

if __name__ == '__main__':
    getPermutationCount()