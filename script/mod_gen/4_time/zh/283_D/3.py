def main():
    s = input()
    s = s.replace('()', '')
    while True:
        t = s.replace('()', '')
        if t == s:
            break
        else:
            s = t
    if len(s) == 0:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()