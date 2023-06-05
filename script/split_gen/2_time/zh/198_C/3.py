def check(n):
    n_str = str(n)
    n_str_rev = n_str[::-1]
    if n_str == n_str_rev:
        return True
    else:
        return False
