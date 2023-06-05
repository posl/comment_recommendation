def main():
    date = input()
    year = int(date.split('/')[0])
    month = int(date.split('/')[1])
    day = int(date.split('/')[2])
    if year < 2019:
        print('Heisei')
    elif year == 2019 and month <= 4 and day <= 30:
        print('Heisei')
    else:
        print('TBD')
