def main():
    s = input()
    if '0' in s or '1' in s or '2' in s:
        print('Yes')
    elif len(s) >= 2 and ('0' in s[1:] or '1' in s[1:] or '2' in s[1:]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()