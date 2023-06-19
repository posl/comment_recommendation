def is_polygon(n, l):
    if max(l) < sum(l) - max(l):
        return True
    else:
        return False

if __name__ == '__main__':
    is_polygon()