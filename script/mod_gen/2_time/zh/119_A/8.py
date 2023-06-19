def main():
    s = input()
    year, month, day = map(int, s.split('/'))
    if year < 2019:
        print('Heisei')
    elif year > 2019:
        print('TBD')
    elif month < 4:
        print('Heisei')
    elif month > 4:
        print('TBD')
    elif day <= 30:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()