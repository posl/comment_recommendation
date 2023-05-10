def main():
    s = input()
    year, month, day = s.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) > 2019:
        print('TBD')
    else:
        if int(month) < 4:
            print('Heisei')
        elif int(month) > 4:
            print('TBD')
        else:
            if int(day) <= 30:
                print('Heisei')
            else:
                print('TBD')
