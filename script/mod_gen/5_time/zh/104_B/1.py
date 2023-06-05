def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1] == 'C' or s[-1] == 'C':
        print('WA')
        return
    for i in range(1, len(s)):
        if s[i] == 'C':
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')
main()
