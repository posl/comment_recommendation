def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower() == True:
        print('AC')
    else:
        print('WA')
main()

if __name__ == '__main__':
    main()