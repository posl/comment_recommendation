def main():
    s = input()
    if s[0] == '0':
        if s[1] == '0':
            print('NA')
        else:
            if s[2] == '0':
                if s[3] == '0':
                    print('NA')
                else:
                    print('YYMM')
            else:
                if s[3] == '0':
                    print('NA')
                else:
                    print('AMBIGUOUS')
    else:
        if s[1] == '0':
            if s[2] == '0':
                if s[3] == '0':
                    print('NA')
                else:
                    print('MMYY')
            else:
                if s[3] == '0':
                    print('NA')
                else:
                    print('AMBIGUOUS')
        else:
            if s[2] == '0':
                if s[3] == '0':
                    print('NA')
                else:
                    print('YYMM')
            else:
                if s[3] == '0':
                    print('NA')
                else:
                    print('AMBIGUOUS')

if __name__ == '__main__':
    main()