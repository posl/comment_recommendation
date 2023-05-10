def can_draw_polygon(L):
    L.sort()
    if L[-1] < sum(L[:-1]):
        return True
    else:
        return False

if __name__ == '__main__':
    can_draw_polygon()