def get_char(n, x):
    if x <= n:
        return chr(64 + x)
    else:
        return get_char(n, x - n)
