def getProbability(A, B, C, X):
    if X <= A:
        return 1
    elif X > B:
        return 0
    else:
        return C/(B-A)

if __name__ == '__main__':
    getProbability()