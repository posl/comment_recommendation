def main():
    s = input()
    a = ord('A') - 1
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - a) * (26 ** (len(s) - i - 1))
    print(ans)

if __name__ == '__main__':
    main()