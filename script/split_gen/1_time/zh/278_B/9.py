def main():
    h, m = map(int, input().split())
    while True:
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
        if int(str(h)[::-1]) < 60 and int(str(m)[::-1]) < 24:
            print("%02d:%02d" % (h, m))
            break
