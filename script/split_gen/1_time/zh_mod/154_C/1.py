def is_all_different(n, a):
    a.sort()
    for i in range(0, n-1):
        if a[i] == a[i+1]:
            return False
    return True
