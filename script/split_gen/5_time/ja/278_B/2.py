def main():
    h, m = map(int, input().split())
    while True:
        if m == 59:
            h += 1
            m = 0
        else:
            m += 1
        if h == 24:
            h = 0
        if str(h)[::-1] == str(m):
            print("{0:02d} {1:02d}".format(h, m))
            break
