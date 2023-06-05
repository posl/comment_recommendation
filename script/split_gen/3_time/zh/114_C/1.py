def is753(n):
    n = str(n)
    if n.count('7') > 0 and n.count('5') > 0 and n.count('3') > 0:
        return True
    else:
        return False
