def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
    elif len(S) == 2:
        if int(S) % 8 == 0:
            print('Yes')
        elif int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(112, 1000, 8):
            if str(i).count('0') == 0 and str(i).count('1') == 0 and str(i).count('2') == 0:
                if str(i)[0] in S and str(i)[1] in S and str(i)[2] in S:
                    print('Yes')
                    exit()
        print('No')

if __name__ == '__main__':
    main()