def find(a, x):
    if a[x] == x:
        return x
    else:
        a[x] = find(a, a[x])
        return a[x]
