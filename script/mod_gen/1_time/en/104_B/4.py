def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A', '').replace('C', '')
        if s.islower():
            print('AC')
            return
    print('WA')

if __name__ == '__main__':
    main()