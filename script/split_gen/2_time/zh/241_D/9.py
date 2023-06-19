def insert(x):
    global n
    n += 1
    a[n] = x
    i = n
    while i > 1:
        if a[i] < a[i // 2]:
            a[i], a[i // 2] = a[i // 2], a[i]
            i //= 2
        else:
            break
