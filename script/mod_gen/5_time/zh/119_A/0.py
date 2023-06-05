def main():
    S = input()
    y,m,d = S.split('/')
    if int(y)<2019:
        print('Heisei')
    elif int(m)<4:
        print('Heisei')
    elif int(d)<=30:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()