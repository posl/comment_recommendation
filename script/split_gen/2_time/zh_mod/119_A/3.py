def main():
    S = input()
    year, month, day = S.split('/')
    if int(year) < 2019:
        print('Heisei')
