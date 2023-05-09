def get_generation(n, p):
    if p[n] == 1:
        return 1
    else:
        return get_generation(n, p) + 1
