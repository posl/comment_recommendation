def main():
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            print('No')
            return
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()