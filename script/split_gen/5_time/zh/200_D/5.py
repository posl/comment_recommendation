def check(a,b,c):
    sumb = 0
    sumc = 0
    for i in b:
        sumb += a[i-1]
    for i in c:
        sumc += a[i-1]
    if sumb%200 == sumc%200:
        return True
    else:
        return False
