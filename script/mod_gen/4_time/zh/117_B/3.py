def check_polygon(L):
    max_L = max(L)
    sum_L = sum(L)
    if max_L < sum_L - max_L:
        return "是"
    else:
        return "否"

if __name__ == '__main__':
    check_polygon()