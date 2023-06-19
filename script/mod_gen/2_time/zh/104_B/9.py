def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(len(s)):
        if i != 0 and i != 1 and i != s.index('C') and s[i].isupper():
            print('WA')
            return
    print('AC')
    return

if __name__ == '__main__':
    main()