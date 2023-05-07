def main():
    s = input()
    s = s.split('/')
    if int(s[0]) > 2019:
        print('TBD')
    elif int(s[0]) == 2019:
        if int(s[1]) > 4:
            print('TBD')
        elif int(s[1]) == 4:
            if int(s[2]) > 30:
                print('TBD')
            else:
                print('Heisei')
        else:
            print('Heisei')
    else:
        print('Heisei')

if __name__ == '__main__':
    main()