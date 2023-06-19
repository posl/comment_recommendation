def main():
    s = input()
    s = s.replace('()', '')
    while '()' in s:
        s = s.replace('()', '')
    if s == '':
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()