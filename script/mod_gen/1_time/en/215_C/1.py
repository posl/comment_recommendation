def next_permutation(a):
    for i in range(len(a) - 2, -1, -1):
        if a[i] < a[i + 1]:
            break
    else:
        return False
    for j in range(len(a) - 1, i, -1):
        if a[i] < a[j]:
            break
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[i + 1:][::-1]
    return True

if __name__ == '__main__':
    next_permutation()