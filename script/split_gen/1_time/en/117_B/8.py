def polygon(n, l):
    #print(n, l)
    l.sort()
    #print(l)
    if l[-1] < sum(l[:-1]):
        return "Yes"
    else:
        return "No"
