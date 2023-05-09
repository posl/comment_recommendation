def main():
    s = input()
    if len(s) % 2 == 0:
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == 'L':
                    print('No')
                    exit()
            else:
                if s[i] == 'R':
                    print('No')
                    exit()
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == 'R':
                    print('No')
                    exit()
            else:
                if s[i] == 'L':
                    print('No')
                    exit()
    print('Yes')

if __name__ == '__main__':
    main()