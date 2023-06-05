def inner_grade(n, r):
    if n >= 10:
        return r
    else:
        return r + (10 - n) * 100
