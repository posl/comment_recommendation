def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return
        s = s[1:] + s[0]
    print('No')
    return

if __name__ == '__main__':
    main()