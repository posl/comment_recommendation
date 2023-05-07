def main():
    s = input()
    s_list = s.split('/')
    if int(s_list[1]) <= 4:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()