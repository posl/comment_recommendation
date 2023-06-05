def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    q = s.count("?")
    ans = 0
    for i in range(n):
        if s[i] == "B" or s[i] == "?":
            ans += pow(3, q, mod) * pow(3, i, mod)
            q -= 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()