def main():
    s = input()
    s = s.replace('/','')
    if int(s) >= 20190430:
        print('TBD')
    else:
        print('Heisei')

if __name__ == '__main__':
    main()