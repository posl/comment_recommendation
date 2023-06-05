def hamburger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + hamburger(n-1,n-1):
        return hamburger(n-1,x-1)
    elif x == 2 + hamburger(n-1,n-1):
        return 1 + hamburger(n-1,n-1)
    elif x <= 2 + 2 * hamburger(n-1,n-1):
        return 1 + hamburger(n-1,x-2-hamburger(n-1,n-1))
    else:
        return 2 * hamburger(n-1,n-1) + 1
n,x = map(int,input().split())
print(hamburger(n,x))
