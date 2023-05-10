def check(n):
    return all([n.count(i) >= 1 for i in '753'])
