def main():
    s = input()
    s1 = s[2:]
    s2 = s[:2]
    if 1 <= int(s1) <= 12 and 1 <= int(s2) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s1) <= 12:
        print('YYMM')
    elif 1 <= int(s2) <= 12:
        print('MMYY')
    else:
        print('NA')

if __name__ == '__main__':
    main()