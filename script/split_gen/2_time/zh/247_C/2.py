def getSn(n):
    if n == 1:
        return [1]
    else:
        return getSn(n-1) + [n] + getSn(n-1)
