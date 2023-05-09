def main():
    s = input()
    if s[0] == '1':
        print('No')
        return
    if s[1] == '1' and s[2] == '1':
        print('Yes')
        return
    if s[3] == '1' and s[4] == '1':
        print('Yes')
        return
    if s[5] == '1' and s[6] == '1' and s[7] == '1':
        print('Yes')
        return
    if s[8] == '1' and s[9] == '1':
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()