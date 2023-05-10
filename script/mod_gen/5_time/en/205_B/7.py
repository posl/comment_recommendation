def isPermutation(N, A):
    if len(A) != N:
        return False
    if len(set(A)) != N:
        return False
    if min(A) != 1:
        return False
    if max(A) != N:
        return False
    return True

if __name__ == '__main__':
    isPermutation()