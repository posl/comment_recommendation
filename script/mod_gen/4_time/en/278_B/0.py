def main():
    h, m = map(int, input().split())
    while True:
        if m == 59:
            if h == 23:
                h = 0
            else:
                h += 1
            m = 0
        else:
            m += 1
        if h // 10 == m % 10 and h % 10 == m // 10:
            print(f'{h:02d}:{m:02d}')
            return

if __name__ == '__main__':
    main()