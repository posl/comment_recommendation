def get_blue_jewel_count(n, x, y):
    if y >= x:
        return 0
    else:
        return (n-1) * (y + (n-2) * (x-y))
