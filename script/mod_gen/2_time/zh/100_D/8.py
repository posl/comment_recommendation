def cal_abs_max(l):
    l = sorted(l, key=abs, reverse=True)
    return sum(l[:3])

if __name__ == '__main__':
    cal_abs_max()