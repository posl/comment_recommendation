def worktime(n, a, b):
    #a.sort()
    #b.sort()
    #print(a)
    #print(b)
    #if a[n-1] > b[n-1]:
    #    return a[n-1]
    #else:
    #    return b[n-1]
    time = 0
    for i in range(n):
        if a[i] > b[i]:
            time += a[i]
        else:
            time += b[i]
    return time
