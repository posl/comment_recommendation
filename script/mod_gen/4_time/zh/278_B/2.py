def main():
    h, m = map(int, input().split())
    while True:
        if m < 59:
            m += 1
        else:
            m = 0
            if h < 23:
                h += 1
            else:
                h = 0
        if str(h).zfill(2)[::-1] == str(m).zfill(2):
            print(str(h).zfill(2) + ':' + str(m).zfill(2))
            break

if __name__ == '__main__':
    main()