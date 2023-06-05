def inner_grade(n,r):
    inner = 0
    if n >= 10:
        inner = r
    else:
        inner = r + (10 - n) * 100
    return inner
