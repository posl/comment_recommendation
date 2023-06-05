def isPolygon(L):
    if max(L) < sum(L) - max(L):
        return True
    else:
        return False

if __name__ == '__main__':
    isPolygon()