def next_permutation(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i+1]:
        i -= 1
    if i == -1:
        return False
    j = len(a) - 1
    while a[i] >= a[j]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True

if __name__ == '__main__':
    next_permutation()