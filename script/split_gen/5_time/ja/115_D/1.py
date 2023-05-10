def burger(n):
    if n == 0:
        return 'P'
    return burger(n-1) + 'B' + burger(n-1) + 'P' + burger(n-1) + 'B'
