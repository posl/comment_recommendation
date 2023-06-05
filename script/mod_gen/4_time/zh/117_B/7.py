def is_polygon(n, ls):
    ls.sort()
    if ls[-1] < sum(ls[:-1]):
        return '是'
    else:
        return '否'

if __name__ == '__main__':
    is_polygon()