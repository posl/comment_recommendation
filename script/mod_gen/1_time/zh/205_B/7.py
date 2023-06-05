def check_permutation(N, A):
    if N != len(A):
        return False
    else:
        for i in range(N):
            if i+1 not in A:
                return False
        return True

if __name__ == '__main__':
    check_permutation()