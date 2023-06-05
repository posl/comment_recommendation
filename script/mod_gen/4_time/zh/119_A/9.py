def main():
    date = input()
    year = int(date.split('/')[0])
    month = int(date.split('/')[1])
    day = int(date.split('/')[2])
    if year < 2019:
        print('Heisei')
    elif year > 2019:
        print('TBD')
    else:
        if month <= 4:
            print('Heisei')
        else:
            print('TBD')

if __name__ == '__main__':
    main()