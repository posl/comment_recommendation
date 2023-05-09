def main():
    h, m = map(int, input().split())
    while True:
        if (m % 10) * 10 + (m // 10) < 60:
            if (m % 10) * 10 + (m // 10) >= h:
                print(h, m)
                break
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0

if __name__ == '__main__':
    main()