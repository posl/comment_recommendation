def is_permutation(a):
    a.sort()
    for i in range(len(a)):
        if a[i] != i+1:
            return False
    return True

if __name__ == '__main__':
    is_permutation()