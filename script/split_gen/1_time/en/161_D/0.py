def lunlun(n):
    if n%10 == 0:
        return n+1
    elif n%10 == 9:
        return n-1
    else:
        return [n-1,n+1]
