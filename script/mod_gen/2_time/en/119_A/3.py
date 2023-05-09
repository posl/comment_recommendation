def main():
    S = input()
    year = int(S[0:4])
    month = int(S[5:7])
    day = int(S[8:10])
    if year < 2019:
        print('Heisei')
    elif year == 2019:
        if month < 4:
            print('Heisei')
        elif month == 4:
            if day <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

if __name__ == '__main__':
    main()