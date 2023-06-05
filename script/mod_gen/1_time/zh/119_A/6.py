def main():
    str = input()
    str_list = str.split('/')
    if int(str_list[0]) < 2019:
        print('Heisei')
    elif int(str_list[1]) < 4:
        print('Heisei')
    elif int(str_list[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()