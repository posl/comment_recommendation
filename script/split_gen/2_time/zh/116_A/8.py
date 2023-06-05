def hamburger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + hamburger(n-1, (2**(n+1)-3)//2 + 1):
        return hamburger(n-1, x-1)
    else:
        return 1 + hamburger(n-1, x - (2**(n+1)-3)//2 - 1)
