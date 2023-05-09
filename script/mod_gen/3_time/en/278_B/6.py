def check_confusing_time(h, m):
    h1 = h // 10
    h2 = h % 10
    m1 = m // 10
    m2 = m % 10
    if h1 == m2 and h2 == m1:
        return True
    else:
        return False

if __name__ == '__main__':
    check_confusing_time()