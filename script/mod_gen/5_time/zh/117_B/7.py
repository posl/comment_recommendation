def is_polygon_possible(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    is_polygon_possible()