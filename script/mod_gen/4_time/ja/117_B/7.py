def check_polygon(n, l):
    l.sort(reverse=True)
    max_l = l[0]
    sum_l = sum(l[1:])
    if max_l < sum_l:
        return True
    else:
        return False

if __name__ == '__main__':
    check_polygon()