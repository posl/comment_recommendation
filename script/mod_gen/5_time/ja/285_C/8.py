def main():
    s = input()
    n = len(s)
    if n == 1:
        print(ord(s[0]) - 64)
    elif n == 2:
        print(26 + (ord(s[0]) - 64) * 26 + (ord(s[1]) - 64))
    elif n == 3:
        print(26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 + (ord(s[1]) - 64) * 26 + (ord(s[2]) - 64))
    elif n == 4:
        print(26 * 26 * 26 + 26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 * 26 + (ord(s[1]) - 64) * 26 * 26 + (ord(s[2]) - 64) * 26 + (ord(s[3]) - 64))
    elif n == 5:
        print(26 * 26 * 26 * 26 + 26 * 26 * 26 + 26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 * 26 * 26 + (ord(s[1]) - 64) * 26 * 26 * 26 + (ord(s[2]) - 64) * 26 * 26 + (ord(s[3]) - 64) * 26 + (ord(s[4]) - 64))
    elif n == 6:
        print(26 * 26 * 26 * 26 * 26 + 26 * 26 * 26 * 26 + 26 * 26 * 26 + 26 * 26 + 26 + (ord(s[0]) - 64) * 26 * 26 * 26 * 26 * 26 + (ord(s[1]) - 64) * 26 * 26 * 26 * 26 + (ord(s[2]) - 64) * 26 * 26 * 26 + (ord(s[3]) - 64) * 26 * 26 + (ord(s[4]) - 64) * 26 + (ord(s[5]) - 64

if __name__ == '__main__':
    main()