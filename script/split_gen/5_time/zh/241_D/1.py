def insert(a,x):
    i = 0
    while i < len(a):
        if x <= a[i]:
            break
        i += 1
    a.insert(i,x)
