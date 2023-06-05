def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()