def is_polygon(n,l):
    if n < 3 or n > 10:
        return False
    for i in l:
        if i < 1 or i > 100:
