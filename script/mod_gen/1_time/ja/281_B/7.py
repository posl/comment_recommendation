def main():
    s = input()
    if s[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and s[-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and len(s)==7:
        if s[1:7].isdecimal() and 100000<=int(s[1:7])<=999999:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()