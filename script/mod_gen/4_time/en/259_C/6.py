def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    if len(s) == len(t):
        print('No')
        exit()
    if len(s) < len(t):
        print('No')
        exit()
    while len(s) > len(t):
        if s[-1] == 'a':
            s = s[:-1]
        elif s[-1] == 'b':
            s = s[:-1]
            s = s[::-1]
        else:
            print('No')
            exit()
    if s == t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()