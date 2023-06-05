def main():
    s = input()
    if len(s) == 2:
        if s[0] == 'o' or s[1] == 'o':
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()