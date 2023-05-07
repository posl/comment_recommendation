def is_permutation(N, A):
    if N != len(A):
        return False
    s = set()
    for a in A:
        if a in s:
            return False
        s.add(a)
    return True

if __name__ == '__main__':
    is_permutation()