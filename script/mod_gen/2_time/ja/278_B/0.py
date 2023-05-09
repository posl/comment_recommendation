def main():
    h, m = map(int, input().split())
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        if m // 10 == h % 10 and m % 10 == h // 10:
            break
    print(h, m)

if __name__ == '__main__':
    main()