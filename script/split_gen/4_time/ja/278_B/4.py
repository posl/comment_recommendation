def main():
    h, m = map(int, input().split())
    while True:
        m = m + 1
        if m == 60:
            h = h + 1
            m = 0
        if h == 24:
            h = 0
        if int(str(h)[::-1]) < 60 and h == int(str(m)[::-1]):
            break
    print(h, m)
