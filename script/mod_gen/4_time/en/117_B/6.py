def is_polygon_possible(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    is_polygon_possible()