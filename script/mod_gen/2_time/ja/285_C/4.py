def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += 26 ** i * (ord(s[i]) - ord('A') + 1)
    print(ans)

if __name__ == '__main__':
    main()