def burger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    elif x == 2**n+1:
        return 2**n
    elif x < 2**n+1:
        return burger(n-1,x-1)
    else:
        return 2**n + burger(n-1,x-2**n-1)
