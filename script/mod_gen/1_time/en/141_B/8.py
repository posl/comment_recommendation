def main():
    s = input()
    if s[0] == 'L' or s[1] == 'L':
        print('No')
    elif s[0] == 'R' and s[1] == 'R':
        print('No')
    elif s[0] == 'U' and s[1] == 'D':
        print('No')
    elif s[0] == 'D' and s[1] == 'U':
        print('No')
    elif s[0] == 'U' and s[1] == 'U':
        print('No')
    elif s[0] == 'D' and s[1] == 'D':
        print('No')
    elif s[0] == 'L' and s[1] == 'R':
        print('No')
    elif s[0] == 'R' and s[1] == 'L':
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()