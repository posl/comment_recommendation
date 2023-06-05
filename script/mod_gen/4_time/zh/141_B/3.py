def main():
    s = input()
    if len(s) == 1:
        if s == 'L' or s == 'U' or s == 'D':
            print('No')
        else:
            print('Yes')
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == 'L':
                    print('No')
                    break
            else:
                if s[i] == 'R':
                    print('No')
                    break
        else:
            print('Yes')

if __name__ == '__main__':
    main()