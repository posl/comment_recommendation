def is_polygon(n, l):
    max_l = max(l)
    if max_l < sum(l) - max_l:
        return "是"
    else:
        return "否"

if __name__ == '__main__':
    is_polygon()