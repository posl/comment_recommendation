def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
        return
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            print('No')
            return
    for i in range(len(t), len(s)):
        if s[i] != '?':
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()