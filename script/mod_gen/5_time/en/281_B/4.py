def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdigit() and len(s) == 8 and 100000 <= int(s[1:-1]) <= 999999:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()