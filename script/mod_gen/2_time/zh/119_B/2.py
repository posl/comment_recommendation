def main():
    S = input()
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month <= 4:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()