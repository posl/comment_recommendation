def main():
    S = input()
    if len(S) == 1:
        if S.isupper():
            print('Yes')
        else:
            print('No')
    else:
        if S[0].isupper() and S[-1].isupper():
            if S[1:-1].isdigit():
                if int(S[1:-1]) >= 100000 and int(S[1:-1]) <= 999999:
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')

if __name__ == '__main__':
    main()