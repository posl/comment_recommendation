def main():
    date = input()
    # print(date)
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    # print(year,month,day)
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month <= 4 and day <= 30:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()