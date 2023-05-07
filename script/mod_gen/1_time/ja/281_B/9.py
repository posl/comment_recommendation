def main():
    S = input()
    S = S.replace('0', '1')
    S = S.replace('1', '0')
    S = S.replace('2', '1')
    S = S.replace('3', '1')
    S = S.replace('4', '1')
    S = S.replace('5', '1')
    S = S.replace('6', '1')
    S = S.replace('7', '1')
    S = S.replace('8', '1')
    S = S.replace('9', '1')
    if S == '0':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()