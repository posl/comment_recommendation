def main():
    date = input()
    year, month, day = date.split('/')
    if month == '04' and day == '30':
        print('Heisei')
    elif month == '04' and day < '30':
        print('Heisei')
    elif month < '04':
        print('Heisei')
    else:
        print('TBD')
