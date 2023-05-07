def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    if s[-1] == '1':
        print('No')
        return
    if s[1:-1].count('1') > 1:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()