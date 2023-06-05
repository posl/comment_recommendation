def is_confused_time(h, m):
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10
    if (b == 2 and c == 7 and d == 9) or (b == 5 and c == 9 and d == 2):
        return True
    return False
