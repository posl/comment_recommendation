def main():
    s = input()
    if s[0].isupper() and s[2:8].isdigit() and s[8].isupper():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()