def main():
    S = input()
    S = S.replace('()', '')
    while '()' in S:
        S = S.replace('()', '')
    if len(S) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()