def get_name(n):
    if n <= 26:
        return chr(96 + n)
    else:
        return get_name((n-1)//26) + get_name((n-1)%26 + 1)
