def get_blue_gem_count(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return get_blue_gem_count(n-1, x, y) + get_blue_gem_count(n-2, x, y) + y
