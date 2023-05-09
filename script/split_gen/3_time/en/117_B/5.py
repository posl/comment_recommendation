def polygon(n, l):
    l.sort()
    if l[n-1] < sum(l[:n-1]):
        return 'Yes'
    else:
        return 'No'
