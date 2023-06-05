def main():
    input_date = input()
    year, month, day = input_date.split('/')
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019 and int(month) <= 4:
        print('Heisei')
    else:
        print('TBD')
