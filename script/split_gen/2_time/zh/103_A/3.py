def get_min_cost(a1, a2, a3):
    a = [a1, a2, a3]
    a.sort()
    return a[2] - a[0]
