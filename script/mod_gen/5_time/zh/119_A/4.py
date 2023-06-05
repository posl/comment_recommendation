def main():
    date = input()
    year, month, day = date.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019 and int(month) <= 4 and int(day) <= 30:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()