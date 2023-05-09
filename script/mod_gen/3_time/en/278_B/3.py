def main():
    h, m = map(int, input().split())
    while True:
        if m == 59:
            m = 0
            if h == 23:
                h = 0
            else:
                h += 1
        else:
            m += 1
        if h // 10 == m % 10 and h % 10 == m // 10:
            print('{:0>2d}:{:0>2d}'.format(h, m))
            break

if __name__ == '__main__':
    main()