def main():
    s = input()
    y = int(s.split('/')[0])
    m = int(s.split('/')[1])
    d = int(s.split('/')[2])
    if y < 2019:
        print('Heisei')
    elif y > 2019:
        print('TBD')
    elif y == 2019:
        if m < 4:
            print('Heisei')
        elif m > 4:
            print('TBD')
        elif m == 4:
            if d <= 30:
                print('Heisei')
            else:
                print('TBD')
    return

if __name__ == '__main__':
    main()