def main():
    date = input()
    date_list = date.split('/')
    if int(date_list[0]) < 2019:
        print('Heisei')
    elif int(date_list[0]) == 2019:
        if int(date_list[1]) < 4:
            print('Heisei')
        elif int(date_list[1]) == 4:
            if int(date_list[2]) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

if __name__ == '__main__':
    main()