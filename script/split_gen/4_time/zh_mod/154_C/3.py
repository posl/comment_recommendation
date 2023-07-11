def check_pair(n, a):
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            return False
    return True
