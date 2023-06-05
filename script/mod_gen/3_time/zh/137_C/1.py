def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        s[i] = ''.join(sorted(s[i]))
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()