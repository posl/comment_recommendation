def isConfusingTime(h, m):
    if h == 0 and m == 0:
        return True
    if h == 1 and m == 1:
        return True
    if h == 2 and m == 5:
        return True
    if h == 5 and m == 2:
        return True
    if h == 8 and m == 8:
        return True
    if h == 0 and m == 8:
        return True
    if h == 1 and m == 0:
        return True
    if h == 1 and m == 1:
        return True
    if h == 1 and m == 8:
        return True
    if h == 2 and m == 0:
        return True
    if h == 2 and m == 1:
        return True
    if h == 2 and m == 8:
        return True
    if h == 5 and m == 0:
        return True
    if h == 5 and m == 1:
        return True
    if h == 5 and m == 8:
        return True
    if h == 8 and m == 0:
        return True
    if h == 8 and m == 1:
        return True
    if h == 8 and m == 8:
        return True
    return False

if __name__ == '__main__':
    isConfusingTime()