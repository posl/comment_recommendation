def get_S(n):
    if n == 1:
        return [1]
    else:
        return get_S(n-1) + [n] + get_S(n-1)
