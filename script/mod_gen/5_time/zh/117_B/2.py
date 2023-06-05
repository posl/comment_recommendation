def check_polygon(n, l):
    max_l = max(l)
    sum_l = sum(l) - max_l
    if max_l < sum_l:
        return "是"
    else:
        return "否"

if __name__ == '__main__':
    check_polygon()