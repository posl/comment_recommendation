def burger(n,x):
    if x == 1:
        return 0
    elif n == 1:
        return 1
    else:
        if x <= 2**n-2**(n-1)+1:
            return burger(n-1,x-1)
        else:
            return 2**(n-1)+burger(n-1,x-2**(n-1))+1
