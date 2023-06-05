def main():
    h, m = [int(x) for x in input().split()]
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
        if int(str(m).zfill(2)[::-1]) == h:
            break
    print(f'{h} {m}')

if __name__ == '__main__':
    main()