def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1, len(s)):
            if s[i] == 'C':
                continue
            if s[i].isupper():
                print('WA')
                return
        print('AC')
    else:
        print('WA')

if __name__ == '__main__':
    main()