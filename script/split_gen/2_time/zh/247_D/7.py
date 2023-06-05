def get_s(n):
    if n == 1:
        return [1]
    else:
        return get_s(n-1) + [n] + get_s(n-1)
