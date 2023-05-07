def is_permutation(N, A):
    # N: number of integers in A
    # A: list of integers
    # return: True if A is a permutation of (1, 2, ..., N)
    #         False otherwise
    # write your code here
    # replace the following line with your code
    # return True
    # write your code here
    # replace the following line with your code
    # return True
    if len(A) != N:
        return False
    if len(set(A)) != N:
        return False
    if set(A) != set(range(1, N + 1)):
        return False
    return True

if __name__ == '__main__':
    is_permutation()