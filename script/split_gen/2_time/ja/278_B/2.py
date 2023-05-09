def main():
    h, m = map(int, input().split())
    while True:
        if m == 59:
            if h == 23:
                h = 0
                m = 0
            else:
                h += 1
                m = 0
        else:
            m += 1
        if str(h) == str(m)[::-1]:
            print(str(h).zfill(2), str(m).zfill(2))
            break
