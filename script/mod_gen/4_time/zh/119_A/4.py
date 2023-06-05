def main():
    S = input()
    year, month, day = S.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019:
        if int(month) < 4:
            print('Heisei')
        elif int(month) == 4:
            if int(day) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

if __name__ == '__main__':
    main()