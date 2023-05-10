def check_polygon(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    check_polygon()