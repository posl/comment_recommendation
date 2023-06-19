def is_permutation(A):
    if len(A) == 1:
        return True
    else:
        B = []
        for i in range(1, len(A)+1):
            B.append(i)
        A.sort()
        if A == B:
            return True
        else:
            return False

if __name__ == '__main__':
    is_permutation()