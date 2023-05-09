def main():
    k = int(input())
    h = 21
    m = 0
    while k > 0:
        m += 1
        k -= 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
    print('%02d:%02d' % (h, m))
