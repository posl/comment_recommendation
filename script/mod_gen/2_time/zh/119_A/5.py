def main():
    date = list(map(int, input().split('/')))
    if date[0] < 2019:
        print('Heisei')
    elif date[1] < 4:
        print('Heisei')
    elif date[2] <= 30:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()