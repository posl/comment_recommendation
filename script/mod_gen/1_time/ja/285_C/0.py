def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i]) - ord('A') + 1) * (26 ** (n - 1 - i))
    print(ans)

if __name__ == '__main__':
    main()