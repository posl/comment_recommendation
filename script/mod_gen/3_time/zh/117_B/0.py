def is_polygon(n, l):
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        return True
    else:

if __name__ == '__main__':
    is_polygon()