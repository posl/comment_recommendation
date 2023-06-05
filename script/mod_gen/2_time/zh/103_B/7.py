def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return
        s = s[1:] + s[0]
    print('No')

if __name__ == '__main__':
    main()