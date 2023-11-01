def isPolygon(a):
    a.sort(reverse=True)
    if a[0] < sum(a[1:]):
        return True
    else:
        return False

if __name__ == '__main__':
    isPolygon()