def isPermutation(N, A):
    if N != len(A):
        return False
    if len(set(A)) != N:
        return False
    for i in range(N):
        if i+1 not in A:
            return False
    return True

if __name__ == '__main__':
    isPermutation()