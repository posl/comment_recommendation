def main():
    S = input()
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
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
