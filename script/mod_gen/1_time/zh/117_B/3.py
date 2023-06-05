def is_polygon(n, L):
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        return True
    else:
        return False

if __name__ == '__main__':
    is_polygon()