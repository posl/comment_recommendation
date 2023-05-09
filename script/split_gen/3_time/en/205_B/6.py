def check_permutation(n, a):
    a.sort()
    for i in range(n):
        if i+1 != a[i]:
            return 'No'
    return 'Yes'
