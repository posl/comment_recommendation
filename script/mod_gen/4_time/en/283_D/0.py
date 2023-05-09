def main():
    s = input()
    s = s.replace('()', '')
    while '()' in s:
        s = s.replace('()', '')
    if len(s) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()