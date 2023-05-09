def isArithmeticSequence(A):
    A = sorted(A)
    if A[2] - A[1] == A[1] - A[0]:
        return True
    else:
        return False

if __name__ == '__main__':
    isArithmeticSequence()