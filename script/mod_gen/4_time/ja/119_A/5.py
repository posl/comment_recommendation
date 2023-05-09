def judge():
    s = input()
    s = s.split('/')
    if int(s[0]) > 2019:
        print('TBD')
    elif int(s[1]) > 4:
        print('TBD')
    elif int(s[2]) > 30:
        print('TBD')
    else:
        print('Heisei')
judge()

if __name__ == '__main__':
    judge()