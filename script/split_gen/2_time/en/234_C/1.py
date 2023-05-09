def make_2s(n):
    if n == 0:
        return ['']
    else:
        return ['0' + x for x in make_2s(n-1)] + ['2' + x for x in make_2s(n-1)]
