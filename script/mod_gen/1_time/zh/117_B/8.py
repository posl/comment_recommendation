def check_polygon(l):
    max_l = max(l)
    sum_l = sum(l) - max_l
    if max_l < sum_l:
        return True
    else:
        return False

if __name__ == '__main__':
    check_polygon()