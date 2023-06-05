def main():
    s = input()
    if len(s) == 4 and s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()