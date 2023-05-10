def main():
    s = input()
    y, m, d = s.split('/')
    y = int(y)
    m = int(m)
    d = int(d)
    if y < 2019:
        print('Heisei')
    elif y == 2019 and m <= 4:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()