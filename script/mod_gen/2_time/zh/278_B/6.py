def isConfusingTime(h,m):
    h1 = h//10
    h2 = h%10
    m1 = m//10
    m2 = m%10
    if h1 == 2 and h2 == 0 and m1 == 0 and m2 == 0:
        return True
    if h1 == 0 and h2 == 0 and m1 == 0 and m2 == 0:
        return True
    if h1 == 1 and h2 == 2 and m1 == 0 and m2 == 0:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 1:
        return True
    if h1 == 1 and h2 == 1 and m1 == 0 and m2 == 6:
        return True
    if h1 == 1 and h2 == 1 and m1 == 0 and m2 == 9:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 6:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 9:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 8:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 3:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 4:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 5:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 7:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 2:
        return True
    if h1 == 1 and h2 == 1 and m1 == 1 and m2 == 0:
        return True
    if h1 == 1 and h2 ==

if __name__ == '__main__':
    isConfusingTime()