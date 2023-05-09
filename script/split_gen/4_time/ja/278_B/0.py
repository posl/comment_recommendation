def main():
    h, m = map(int, input().split())
    while True:
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
        if str(h)[0] == str(m)[1] and str(h)[1] == str(m)[0]:
            print(str(h).zfill(2), str(m).zfill(2))
            break
