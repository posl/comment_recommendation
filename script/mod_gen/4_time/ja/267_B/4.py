def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    if s[3] == '0' and s[4] == '0':
        print('No')
        return
    if s[6] == '0' and s[7] == '0':
        print('No')
        return
    if s[9] == '0':
        print('No')
        return
    print('Yes')

if __name__ == '__main__':
    main()