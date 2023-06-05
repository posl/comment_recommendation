def get_num(n):
    if n < 2:
        return str(n)
    else:
        return get_num(n//2) + str(n%2)
