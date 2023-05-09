def is_permutation(A):
    return len(set(A)) == len(A) and max(A) == len(A)

if __name__ == '__main__':
    is_permutation()