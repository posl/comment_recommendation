def main():
    h, m = map(int, input().split())
    if m >= 30:
        h += 1
        m -= 30
    else:
        m += 30
    if h == 24:
        h = 0
    print("{0:02d} {1:02d}".format(h, m))
