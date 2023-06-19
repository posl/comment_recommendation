def is_drawable(n, l):
    # l.sort()
    max_l = max(l)
    sum_l = sum(l) - max_l
    return max_l < sum_l

if __name__ == '__main__':
    is_drawable()