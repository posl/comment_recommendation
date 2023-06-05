def next_permutation(a):
    # Find non-increasing suffix
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    
    # Reverse suffix
    a[i : ] = a[len(a) - 1 : i - 1 : -1]
    return True

if __name__ == '__main__':
    next_permutation()