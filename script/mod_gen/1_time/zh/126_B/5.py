def main():
    s = input()
    # print(s)
    # print(s[0:2])
    # print(s[2:4])
    # print(s[0:2] in range(1,13))
    # print(s[2:4] in range(1,13))
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s[0:2]) <= 12 and not 1 <= int(s[2:4]) <= 12:
        print('MMYY')
    elif not 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')

if __name__ == '__main__':
    main()