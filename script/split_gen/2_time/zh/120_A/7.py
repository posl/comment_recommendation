def max_count(a,b,c):
    count = 0
    if c > b // a:
        count = b // a
    else:
        count = c
    return count
