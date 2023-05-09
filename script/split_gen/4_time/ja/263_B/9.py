def calc_generation(n, parents, child):
    if n == 1:
        return 0
    else:
        return calc_generation(n-1, parents, child) + 1
