def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return 0
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return 0
        else:
            s = s[-1] + s[:-1]
    print('No')

if __name__ == '__main__':
    main()