def split(n):
    n_str = str(n)
    n_len = len(n_str)
    max = 0
    for i in range(1, n_len):
        a = int(n_str[:i])
        b = int(n_str[i:])
        if a * b > max:
            max = a * b
    return max
