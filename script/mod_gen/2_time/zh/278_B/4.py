def is_confused_time(h, m):
    h1 = int(h / 10)
    h2 = h % 10
    m1 = int(m / 10)
    m2 = m % 10
    if h1 == 2 and h2 == 3 and m1 == 5 and m2 == 9:
        return True
    if h1 == 5 and h2 == 9 and m1 == 5 and m2 == 9:
        return True
    if h1 == 2 and h2 == 3 and m1 == 2 and m2 == 3:
        return True
    if h1 == 5 and h2 == 9 and m1 == 2 and m2 == 3:
        return True
    return False

if __name__ == '__main__':
    is_confused_time()