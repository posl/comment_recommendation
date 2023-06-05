def is_confusing_time(h, m):
    h1 = int(str(m)[1])
    m1 = int(str(h)[1])
    if h1 == m1:
        return False
    h2 = int(str(m)[0])
    m2 = int(str(h)[0])
    if h2 == m2:
        return False
    if h1 == m2:
        return False
    if h2 == m1:
        return False
    return True

if __name__ == '__main__':
    is_confusing_time()