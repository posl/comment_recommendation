def main():
    s = input()
    if len(s) == 1:
        if s.islower():
            print('Yes')
        else:
            print('No')
    else:
        if s[0::2].islower() and s[1::2].isupper():
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()