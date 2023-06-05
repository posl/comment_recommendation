def main():
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])
    for i in range(26):
        print(chr(s[i]+96), end = '')

if __name__ == '__main__':
    main()