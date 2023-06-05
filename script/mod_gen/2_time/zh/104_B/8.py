def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A','')
        s = s.replace('C','')
        if s.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')

if __name__ == '__main__':
    main()