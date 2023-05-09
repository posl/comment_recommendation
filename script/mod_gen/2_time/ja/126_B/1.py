def main():
    s = input()
    if s[0] == '0' and s[1] == '0':
        if s[2] == '0' or s[3] == '0':
            print('NA')
        else:
            print('MMYY')
    elif s[0] == '0' or s[1] == '0':
        if s[2] == '0' and s[3] == '0':
            print('NA')
        else:
            print('YYMM')
    else:
        if s[2] == '0' or s[3] == '0':
            print('YYMM')
        else:
            print('AMBIGUOUS')

if __name__ == '__main__':
    main()