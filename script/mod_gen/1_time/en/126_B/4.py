def main():
    s = input()
    if int(s[:2]) > 12:
        if int(s[2:]) > 12:
            print('NA')
        else:
            print('YYMM')
    else:
        if int(s[2:]) > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')

if __name__ == '__main__':
    main()